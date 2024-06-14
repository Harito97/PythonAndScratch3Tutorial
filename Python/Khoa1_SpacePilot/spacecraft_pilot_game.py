import math, random, sys, pygame

# Khởi tạo đối tượng pygame
pygame.init()

# Khởi tạo đối tượng màn hình có kích thước tùy chỉnh
screen = pygame.display.set_mode((800, 700))

# Đặt tên cho cửa sổ màn hình
pygame.display.set_caption("Spacecraft Pilot Game")

# Thiết lập thông tin thuộc tính cho tàu vũ trụ
spacecraft_img = pygame.image.load("resources/Spacecraft_Img.png")
spacecraft_img = pygame.transform.scale(spacecraft_img, (350, 150))
pygame.display.set_icon(spacecraft_img)
start_x = 250
start_y = 550
spacecraft_core_x = start_x + 350 / 2
spacecraft_core_y = start_y + 150 / 2
x_change = 0
y_change = 0
current_x = 0
current_y = 0

# Thiết lập phông nền
background_img = pygame.image.load("resources/universe_15.jpg")
background_img = pygame.transform.scale(background_img, (800, 700))

# Thiết lập thông tin thuộc tính của thiên thạch
meteor_img = pygame.image.load("resources/meteoroid-asteroid-rock-outcrop_0.png")
meteor_img = pygame.transform.scale(meteor_img, (50, 50))
meteor_x = 375
meteor_y = 0
meteor_core_x = meteor_x + 50 / 2
meteor_core_y = meteor_y + 50 / 2

# Thiết lập điểm số
score_text = pygame.font.SysFont("TimeNewRoman", 30)

# Thiết lập tiếng nổ kết thúc trò chơi
explosion_sound = pygame.mixer.Sound("resources/397691__morganpurkis__explosion.wav")

# Thiết lập vụ nổ
explosion_img = pygame.image.load("resources/bumm.png")
explosion_img = pygame.transform.scale(explosion_img, (400, 200))

# Thiết lập flag
game_over = False
score = 0
number_life = 3

while True:
    # Xử lý event điều khiển tàu bằng bấm phím
    for event in pygame.event.get():
        # Xử lý việc kết thúc chương trình nếu bấm thoát
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
            elif event.key == pygame.K_DOWN:
                y_change = 5
            elif event.key == pygame.K_UP:
                y_change = -5
        if event.type == pygame.KEYUP:
            x_change = 0
            y_change = 0

    screen.blit(background_img, (0, 0))
    if not game_over:
        current_x = start_x + x_change
        current_y = start_y + y_change
        if (0 <= current_x <= 450) and (0 <= current_y <= 550):
            start_x = current_x
            start_y = current_y
        meteor_y += 2

        # Xử lý khởi tạo thiên thạch và cộng điểm
        if meteor_y > 700:
            meteor_y = 0
            meteor_x = random.randint(0, 750)
            score += 1

        spacecraft_core_x = start_x + 350 / 2
        spacecraft_core_y = start_y + 150 / 2
        meteor_core_x = meteor_x + 50 / 2
        meteor_core_y = meteor_y + 50 / 2

        distance = math.sqrt(
            (spacecraft_core_x - meteor_core_x) ** 2
            + (spacecraft_core_y - meteor_core_y) ** 2
        )
        if distance < 100 or number_life == 0:
            # <226 vì khoảng cách lớn nhất có va chạm là 25*sqrt(58) + 25*sqrt(2) gần bằng 226
            # <100 vì ước lượng (thực tế khi chơi) - do không phải hình vuông với hình vuông giao nhau
            # đồng thời để đảm bảo độ dễ
            game_over = True
            number_life -= 1
            explosion_sound.play(1, 0, 402)
        screen.blit(meteor_img, (meteor_x, meteor_y))
        screen.blit(spacecraft_img, (start_x, start_y))
    else:
        screen.blit(explosion_img, (meteor_core_x - 200, meteor_core_y))
    score_render = score_text.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_render, (0, 0))
    pygame.display.update()

# Function sẽ thêm: 1. Lựa chọn chơi tiếp sau khi kết thúc 2. Thêm hộp thoại cho phép dừng/tiếp tục chơi và reset
# if game_over:
#     screen.blit(background_img, (0, 0))
#     score_render = score_text.render("Score: " + str(score), True, (255, 255, 255))
#     screen.blit(score_render, (0, 0))
#     screen.blit(explosion_img, (meteor_core_x - 200, meteor_core_y))
#     # Tạo đối tượng phông chữ với kích thước 40
#     font = pygame.font.Font(None, 40)
#
#     # Tạo bề mặt chứa thông điệp của bạn
#     message_surface = font.render("Still play?", True, (255, 255, 255))
#
#     # Tính toán kích thước của hộp chứa thông điệp
#     message_rect = message_surface.get_rect()
#
#     # Đặt vị trí của hộp chứa thông điệp giữa cửa sổ
#     message_rect.center = (400, 300)
#
#     # Vẽ văn bản lên bề mặt của hộp chứa thông điệp
#     screen.blit(message_surface, message_rect)
#
#     # Tạo hộp chứa nút "Yes"
#     yes_rect = pygame.Rect(250, 400, 100, 50)
#     # pygame.draw.rect(screen, (0, 0, 0, 0), yes_rect)
#     yes_surface = font.render("YES", True, (0, 255, 0))
#     yes_rect.center = yes_rect.center
#     screen.blit(yes_surface, yes_rect)
#
#     # Tạo hộp chứa nút "No"
#     no_rect = pygame.Rect(500, 400, 100, 50)
#     # pygame.draw.rect(screen, (0, 0, 0, 0), no_rect)
#     no_surface = font.render("NO", True, (255, 0, 0))
#     no_rect.center = no_rect.center
#     screen.blit(no_surface, no_rect)
#
#     # Cập nhật cửa sổ
#     pygame.display.update()
#
#     # Chờ người dùng nhấn nút "Yes" hoặc "No"
#     flag = True
#     while flag:
#         for event in pygame.event.get():
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if yes_rect.collidepoint(event.pos):
#                     game_over = False
#                     flag = False
#                 elif no_rect.collidepoint(event.pos):
#                     flag = False
#             if not flag:
#                 break

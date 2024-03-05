import pygame, sys # ném thứ viện vô chương trình 
import random 
from math import sqrt
 
pygame.init()                                                           # tạo ra 1 đối tượng pygame
screen = pygame.display.set_mode((720, 480))                            # khởi tạo kích thước cho cửa sổ 
pygame.display.set_caption('Spacecraft Pilot Game of Phuong')           # gán tên cho thanh tiêu đề 

# setup ship 
ship_img = pygame.image.load('resources/Spacecraft_Img.png')            # load ảnh tàu vũ trụ vào chương trình 
ship_img = pygame.transform.scale(ship_img, (400, 200))

pygame.display.set_icon(ship_img)                                       # đặt logo icon của chương trình trên thanh tiêu đề 

# setup background
bg_img = pygame.image.load('resources/universe_15.jpg') # load ảnh nền vô 
bg_img = pygame.transform.scale(bg_img, (720, 480))     # scale hình ảnh cho khít cho đẹp 

# setup thiên thạch 
meteor_img = pygame.image.load('resources/meteoroid-asteroid-rock-outcrop_0.png')
meteor_img = pygame.transform.scale(meteor_img, (40, 40))
meteor_x, meteor_y = random.randint(0, 720), 0

x_change, y_change = 0, 0       # khoi tao bien x_change
ship_x, ship_y = 100, 100       # biến đặt tọa độ cho tàu 
SPEED = 5
score = 0                       # Khoi tao bien score voi gia tri mac dinh la 0

game_over = False
score_text = pygame.font.SysFont('Arial', 20) # tao ra 1 doi tuong text tu pygame

while not game_over:
    for event in pygame.event.get():    # duyệt qua từng sự kiện được bắt gặp trong vòng while 
        if event.type == pygame.QUIT:   # nếu sự kiện là 1 sự kiện kết thúc 
            # thoát chương trình 
            pygame.quit()               # giết chết đói tượng pygame 
            sys.exit()                  # exit khỏi hệ thống 

        # bổ sung sự kiện người dùng bấm phím 
        if event.type == pygame.KEYDOWN:
            # kiểm tra các phím sang trái, phải, lên, xuống 
            if event.key == pygame.K_LEFT:
                x_change = -SPEED
            elif event.key == pygame.K_RIGHT:
                x_change = SPEED
            elif event.key == pygame.K_UP:
                y_change -= SPEED
            elif event.key == pygame.K_DOWN:
                y_change += SPEED
            elif event.key == pygame.K_a:
                x_change = -SPEED
            elif event.key == pygame.K_d:
                x_change = SPEED
            elif event.key == pygame.K_w:
                y_change -= SPEED
            elif event.key == pygame.K_s:
                y_change += SPEED
            elif event.key == pygame.K_SPACE:
                ship_x, ship_y = 0, 0
                x_change, y_change = 0, 0
            
        if event.type == pygame.KEYUP:
            x_change, y_change = 0, 0
        
        # distance = ((ship_x - meteor_x) ** 2 + (ship_y - meteor_y) ** 2) ** (1/2)
        distance = sqrt((ship_x - meteor_x) ** 2 + (ship_y - meteor_y) ** 2)
        
        if distance < 70:
            game_over = True 
        
        if meteor_y > 480:
            # reset lai toa do truc y
            meteor_y = 0
            # đặt giá trị random cho tọa độ x
            meteor_x = random.randint(0, 720)
            score += 1  # update them diem cho nguoi choi -> score = score + 1
      
    ship_x += x_change              # update giá trị của tọa độ x của con tàu 
    ship_y += y_change
    meteor_y += 10
    # start_y + # bvn1. 
    screen.blit(bg_img, (0, 0))     # đặt ảnh nền vô cửa sổ chương trình 
    screen.blit(ship_img, (ship_x, ship_y)) # vẽ tàu lên trên background
    screen.blit(meteor_img, (meteor_x, meteor_y)) # vẽ thiên thạch 
    score_render = score_text.render('Score: ' + str(score), True, (255, 255, 255), (255, 255, 0))
    screen.blit(score_render, (0, 0))

    pygame.display.update()         # update sự hiển thị của đối tượng pygame 

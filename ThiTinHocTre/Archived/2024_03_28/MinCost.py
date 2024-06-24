def find_number_divisor(number: int):
    # đếm số ước lớn hơn 1 của 1 số
    count = 0
    for i in range(number, 1, -1):
        if number % i == 0:
            count += 1
    return count


def find_optimal_path(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Tạo ma trận dp để lưu trữ tổng chi phí tới mỗi ô
    dp = [[0] * cols for _ in range(rows)]

    # Khởi tạo giá trị của ô [0,0]
    dp[0][0] = matrix[0][0]

    # Tính tổng chi phí tới từng ô trong ma trận
    for i in range(rows):
        for j in range(cols):
            # Nếu không phải là ô [0,0]
            if i != 0 or j != 0:
                # Chọn ô có giá trị nhỏ nhất trong hai ô lân cận
                if i == 0:
                    dp[i][j] = dp[i][j - 1] + matrix[i][j]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] + matrix[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + matrix[i][j]

    # Trả về tổng chi phí tới ô đích
    return dp[rows - 1][cols - 1]


# Ma trận đã cho
# matrix = [[1, 2, 1, 1],
#           [3, 1, 3, 2],
#           [3, 1, 2, 2]]

matrix = [
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
]

new_matrix = matrix.copy()
for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        new_matrix[row][col] = find_number_divisor(matrix[row][col])

# Tìm đường đi tối ưu và in ra tổng chi phí
optimal_cost = find_optimal_path(new_matrix)
print("Tổng chi phí của đường đi tối ưu là:", optimal_cost)

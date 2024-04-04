x1, y1 = map(float, input('Nhập vào tọa độ (x1, y1) điểm thứ nhất: ').strip().split())
x2, y2 = map(float, input('Nhập vào tọa độ (x2, y2) điểm thứ hai: ').strip().split())

from math import sqrt
distance = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

print(f'Khoảng cách 2 điểm ({x1}, {y1}) và ({x2}, {y2}) là: {distance}')
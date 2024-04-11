# """Bài 1. Viết 1 hàm cho phép tính căn bậc 2 của 1 số"""
# def sqrt_c1(number):
#     return number ** 0.5

# from math import sqrt
# def sqrt_c2(number):
#     return sqrt(number)

# def main():
#     number = 300
#     print(f'Căn bậc 2 của {number} theo cách 1 là {sqrt_c1(number)}')
#     print(f'Căn bậc 2 của {number} theo cách 2 là {sqrt_c2(number)}')

# if __name__ == '__main__':
#     main()


"""Bài 2. Viết 1 hàm tính bình phương của 1 số"""
def double_c1(number):
    return number ** 2

from math import pow
def double_c2(number):
    return pow(number, 2)

def main():
    number = 300
    print(f'Bình phương của {number} theo cách 1 là {double_c1(number)}')
    print(f'Bình phương của {number} theo cách 2 là {double_c2(number)}')

if __name__ == '__main__':
    main()
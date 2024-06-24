# tinh giai thua
import math
from math import sqrt


def tinh_giai_thua(number: int):
    if number < 0:
        return -1
    elif number == 0:
        return 1
    result = 1
    # ...
    for i in range(1, number + 1, 1):
        result *= i
    return result


def tinh_can_bac_hai(number: int):
    return sqrt(number)


def tinh_mu_bac_hai(number: int):
    return number**2


def nghich_dao_truc_so(number: int):
    return -number


def tinh_dien_tich_hinh_tron(number: float):
    return number * number * math.pi


def tinh_dien_tich_tam_giac_vuong(a, b):
    # a^2 + b^2 = c^2
    return 0.5 * a * b


def tinh_dien_tich_tam_giac_3_canh(a, b, c):
    p = (a + b + c) * 0.5
    return sqrt(p * (p - a) * (p - b) * (p - c))


def tinh_bieu_thuc_tong_so_chinh_phuong(n: int):
    # 1 + 4 + 9 + 16 + 25 + 36 + 49 + ... + (math.sqrt(n)) ** 2
    sum_number = 0
    for i in range(1, int(sqrt(n)) + 1):
        sum_number += i**2
    return sum_number


def check_prime(n: int):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def tinh_tong_cac_so_nguyen_to_tu_1_den_n(n: int):
    result = 0
    if n < 2:
        return result
    for i in range(2, n + 1):
        if check_prime(i):
            result += i
    return result


def check_so_hoan_hao(n: int): 
    if n <= 0:
        return False
    result = 0
    for i in range(1, n):
        if n % i == 0:
            result += i
    return result == n

def print_cac_so_hoan_hao_tu_1_den_n(n: int):
    result = []
    for i in range(n):
        if check_so_hoan_hao(i):
            result.append(i)
    print(result)


if __name__ == "__main__":
    # number = int(input("Nhap vao so number de tinh giai thua cua number: "))
    # print(tinh_giai_thua(number=number))

    # number = int(input("Nhap vao so number de tinh mu bac 2 cua number: "))
    # print(tinh_mu_bac_hai(number=number))

    # list_number = input("Nhap vao 2 number la 2 canh cua tam giac vuong: ").split(' ')
    # number1, number2 = int(list_number[0]), int(list_number[1])
    # print(tinh_dien_tich_tam_giac_vuong(a=number1, b = number2))

    # list_number = input("Nhap vao 3 number la 3 canh cua tam giac: ").split(" ")
    # number1, number2, number3 = (
    #     int(list_number[0]),
    #     int(list_number[1]),
    #     int(list_number[2]),
    # )
    # # a + b > c, b + c > a, c + a > b   # 3 4 5
    # print(tinh_dien_tich_tam_giac_3_canh(a=number1, b=number2, c=number3))

    # number = int(input('Nhap vao 1 so number de tinh tong cac so chinh phuong tu 1 den n: '))
    # print(tinh_bieu_thuc_tong_so_chinh_phuong(number))

    # number = int(input('Nhap vao 1 so number de kiem ra no co la 1 so nguyen to khong: '))
    # print(check_prime(n=number))

    # number = int(
    #     input("Nhap vao 1 so number de tinh tong cac so nguyen to tu 1 den no: ")
    # )
    # print(tinh_tong_cac_so_nguyen_to_tu_1_den_n(n=number))

    number = int(input('Nhập vào số n - test bài số hoàn hảo: '))
    print_cac_so_hoan_hao_tu_1_den_n(n=number)
"""
Bài về nhà:
Nhập vào từ bàn phím 2 số a và b
Tìm ước chung lớn nhất và bội chung nhỏ nhất của a và b
"""


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


def main():
    # Nhập vào hai số từ bàn phím
    a = int(input("Nhập số nguyên dương a: "))
    b = int(input("Nhập số nguyên dương b: "))

    # Tìm ước chung lớn nhất và bội chung nhỏ nhất
    gcd_result = gcd(a, b)
    lcm_result = lcm(a, b)

    # In kết quả
    print(f"Ước chung lớn nhất của {a} và {b} là: {gcd_result}")
    print(f"Bội chung nhỏ nhất của {a} và {b} là: {lcm_result}")


if __name__ == "__main__":
    main()

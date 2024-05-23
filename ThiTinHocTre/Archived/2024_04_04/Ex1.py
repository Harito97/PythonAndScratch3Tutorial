def tinh_toan(a: int, b: int) -> int:
    MOD = 127
    luy_thua_cua_hai = pow(2, a, MOD)
    so_luong_so_hang = b - a + 1
    tong = (
        luy_thua_cua_hai
        * ((pow(2, so_luong_so_hang, MOD) - 1) * pow(2 - 1, MOD - 2, MOD))
    ) % MOD
    return tong


def cach_1(a: int, b: int) -> int:
    """Tính tổng cấp số nhân
    u1 = 2 ** a
    n = b - a + 1
    q = 2
    S = u1 * (1 - q ** n) / (1 - q) = 2 ** a * (2 ** n - 1)
    """
    total_sum = 2**a * (2 ** (b - a + 1) - 1)
    return total_sum % 127


def cach_2(a: int, b: int) -> int:
    """
    # Nhằm tránh tràn số khi phải tính toàn bộ tổng các phần tử trong mảng
    # Với Python thì int là vô hạn (nhưng RAM là hữu hạn) nhưng với C/Java/... thì không thế
    # Bởi vậy chọn kiểu dữ liệu và giải thuật cho phù hợp với input để tiết kiệm bộ nhớ và thời gian tính toán nhanh là bài toán cần suy nghĩ
    a <= 6 -> residual = 2 ** a
    a % 7 == 0 -> residual = 1 = 2 ** 0
    a % 8 == 0 -> residual = 2 = 2 ** 1
    a % 9 ... -> 4 = 2 ** 2
    a % 10 ... -> 8 = 2 ** 3
    ...
    a % 13 ... -> 64 = 2 ** 6
    """
    # total_residual = 0
    # for i in range(a, b + 1):
    #     if i <= 6:
    #         total_residual += 2 ** i
    #     else:
    #         for number in range(7, 14):
    #             if i % number == 0:
    #                 total_residual += 2 ** (number - 7)
    #                 break
    # # print(total_residual)
    # return total_residual % 127
    total_residual = 0
    for i in range(a, b + 1):
        total_residual += (2 ** i % 127)
    return total_residual % 127


if __name__ == "__main__":
    a = int(input("Nhập giá trị a: "))
    b = int(input("Nhập giá trị b: "))
    print(tinh_toan(a, b))
    print(cach_1(a, b))
    print(cach_2(a, b))

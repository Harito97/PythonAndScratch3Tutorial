"""
Bài 1. 
n!! = 1 * 3 * 5 * ... * n với n lẻ 
n!! = 2 * 4 * 6 * ... * n với n chẵn

n là 1 số nhập từ bàn phím
tính n!!
giả định là nếu n <= 0 thì return 1
"""


def double(n: int):
    if n <= 0:
        return 1
    result = 1
    for i in range(n, 0, -2):
        result *= i
    return result

def calculation(n: int):
    sum = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            sum -= double(i)
        else:
            sum += double(i)
    return sum


n = int(input())
print(double(n))

""" 
Bài 2. 
Có 2 điểm trên bề mặt 1 hình cầu.
Tính khoảng cách ngắn nhất để con kiến đi từ điểm này đến điểm kia trên hình cầu.
Khoảng cách Haresine
"""

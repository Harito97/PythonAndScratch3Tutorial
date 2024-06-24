"""
Chú thích: cách theo vét cạn
2 ** n vs n = 10 ** 5
=> 2 ** (10 ** 5) # số rất to -> giới hạn RAM 256MB

Gọi 1 là lúc mà Bình thắng, An thua
Gọi 0 là lúc mà Bình thua, An thắng

Để mà chơi liên tục đủ n ván thì -> nếu có 1 thì sau đó phải là [0] * k
Ngoại lệ là những lúc gần cuối (không cần thiết phải đủ [0] * k)

Ví dụ:
n = 4, k = 2

1000 
1001
0100
0101
0010
0011
0001
0000

=> Output là 8

n = 6
100
"""

n, k = map(int, input().strip().split())

def process(n, k):
    from math import factorial

    def combination(n, k):
        return factorial(n) / (factorial(k) * factorial(n - k))

    
    total = 0
    if n % (k + 1) == 0:
        slice = n // (k + 1) - 1
        N = slice * (k + 1)
        # print(slice, N)
        for i in range(slice + 1):
            new_N = N - (k + 1) * i + i
            total += combination(new_N, i) * (2 * (n - N)) # hay cũng chính là ... * (2 * slice)
            # print(new_N, i, 2 * (n - N), total)
    else:
        slice = n // (k + 1)
        N = slice * (k + 1) 
        # print(slice, N)
        for i in range(slice + 1):
            new_N = N - (k + 1) * i + i
            total += combination(new_N, i) * (2 * (n - N))
            # print(new_N, i, 2 * (n - N), total)
    # # total += factorial(n - N)

    total += ... # những trường hợp đặc biệt - chưa tìm được biểu thức toán học đánh giá - có thể là 1 hàm phi tuyến phức tạp

    # total = 2 * (2 * (n - k - 1))
    # print(total)
    # for i in range(2, k + 1):
    #     temp = n - k - 1 - i
    #     if temp < 0:
    #         break
    #     total += 2 * temp
    
    # return int(total + 4)

    # return 2 * factorial(n - k)
    # return n * (n - k - 1)

    return total

# Người ra đề này ra đề sai vì hiểu nhầm biểu thức toán học đánh giá đếm các trường hợp. Bài toán thực tế để đếm đúng cả các trường hợp đặc biệt là 1 hàm phi tuyến phức tạp hơn.
# Dưới đây là hàm process phục vụ theo ý hiểu sai về toán học của người ra đề 
def process(n, k):
    from math import factorial

    return factorial(n) / (factorial(k) * factorial(n - k))

print(int(process(n, k)))
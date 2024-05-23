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
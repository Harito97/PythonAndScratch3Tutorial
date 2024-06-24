def sum(n:int):
    # n = 2
    sum = 0
    for i in range(0, n):
        # i = 0, 1, 2
        sum += (2 * i + 1)
    return sum 

if __name__ == '__main__':
    '''
    Nhap vao 1 so n la so tu nhien.
    In ra tong: 1 + 3 + 5 + ... + (2 * n + 1)
    '''
    n = int(input('Nhap vao 1 so n - so tu nhien: '))
    print(sum(n))
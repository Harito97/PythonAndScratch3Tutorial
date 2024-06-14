# 1 - 2 + 3 - 4 + 5 - ... + n
def sum(n:int):
    sum = 0
    for i in range(1, n + 1, 1): 
        if i % 2 == 0:
            sum -= i
        else:
            sum += i 
    return sum 

if __name__ == '__main__':
    '''
    Nhap vao 1 so n la so tu nhien.
    In ra tong: 1 - 2 + 3 - 4 + 5 - ... + n
    '''
    n = int(input('Nhap vao 1 so n - so tu nhien: '))
    print(sum(n))
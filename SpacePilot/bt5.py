# tinh 1 + 2 + 3 + 4 + ... + n
def sum(n:int, d:int, x1:int):
    # x1 * n + n * (n - 1) / 2 * d
    return 1 * n + n * (n - 1) / 2 * d

if __name__ == '__main__':
    data = input('Nhap vao n, d, x1: ').split(' ')
    n, d, x1 = int(data[0]), int(data[1]), int(data[2])
    print(sum(n, d, x1))
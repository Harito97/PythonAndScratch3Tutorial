"""
Nhập vào 1 số. Tìm tất cả các ước số của nó
"""

def process(n:int):
    if n < 1:
        return -1
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result

if __name__ == "__main__":
    n = int(input('Nhap vao 1 so: '))
    print(f'Cac uoc so cua {n} la:', process(n=n))
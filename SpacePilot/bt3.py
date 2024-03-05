# review input(), print(), int(), float(), if-else, for, while
# tim so nguyen to lon nhat ma <= 1 so number (so tu nhien) duoc nhap tu ban phim
def find_biggest_prime(number:int):
    result = 0
    if number < 2:
        return -1
    for i in range(number, 1, -1):
        if check_prime(i):
            result = i
            break
    return result

def check_prime(number:int):
    from math import sqrt
    is_prime = True
    # for j in range(2, int(number**0.5) + 1):
    for j in range(2, int(sqrt(number)) + 1):
        if number % j == 0:
            is_prime = False
            break
    return is_prime

if __name__ == '__main__':
    # number = ...
    # print(type(number)) # <class 'ellipsis'>
    number = int(input('Nhap vao 1 so nguyen duong:'))
    print(find_biggest_prime(number))



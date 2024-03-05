# import sys
# print(sys.version)

from math import sqrt 

def distance(A:tuple, B:tuple):
    return sqrt((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2)

if __name__ == '__main__':
    A = (float(input('Nhap x of A.')), float(input('Nhap y of A.')))
    B = (float(input('Nhap x of B.')), float(input('Nhap y of B.')))
    print('Khoang cach A va B la:', distance(A, B))
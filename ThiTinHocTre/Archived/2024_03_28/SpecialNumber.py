# def check(p:int):
#     if p%5==0:
#         p_str=str(p)
#         if len(set(p_str))==len(p_str):
#             return True
#     return False
# n=int(input())
# q=n%5
# count=0
# for stop in range(n-q,0,-5):
#     if check(stop):
#         n=stop
#         break
# for p in range(5,n+1,5):
#     if check(p):
#         count+=1
# print(count)

def check(number:int):
    num_str = str(number)
    return len(set(num_str)) == len(num_str)    # khong co phan tu rieng biet trung nhau 

n = int(input())
count = 0
if n < 5:
    print(0)
else:
    for i in range(5, n + 1, 5):    # 3 10 15 20 ... n (neu n % 5 == 0)
        if check(i):
            print(i, end=' ')
            count += 1
    print(f'\nSo luong so dac biet la: {count}')
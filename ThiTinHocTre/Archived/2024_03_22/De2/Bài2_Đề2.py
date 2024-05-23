# n,k=map(int,input().split())
# s=0
# for i in range(n):
#     s+=int(input())
# if s%k==0:
#     print(s//k)
# else:
#     print(s//k+1)

def read_data_and_calculate(filename:str):
    from math import ceil 
    with open(filename) as f:
        N, K = map(int, f.readline().strip().split())
        data = []
        for i in range(N):
            data.append(int(f.readline()))
        total_water = sum(data)
        need_times = ceil(total_water / K)
    return need_times

def write_data(filename:str, result:float):
    with open(filename, "w") as f:
        f.write(str(int(result)))

if __name__ == "__main__":
    data = read_data_and_calculate(filename='WATERING.INP')
    write_data(filename='WATERING.OUT', result=data)
    print('Lưu output thành công')
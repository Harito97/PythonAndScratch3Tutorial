# n=int(input())
# if n>50:
#     cost=(12000+90000+(n-10)*9000)*90/100
# else:
#     if n>1:
#         cost=12000+10000*(n-1)
#     else:
#         cost=12000
# print(int(cost))

"""
Dữ liệu vào từ file TAXI.INP chứa số nguyên N là số km khách hàng đã đi (1≤ N ≤105).
Kết quả ghi vào file TAXI.OUT số tiền khách hàng phải thanh toán.
"""

def read_data(filename:str):
    with open(filename) as f:
        data = f.readline().strip()
        data = int(data)
    return data

def calculate(data:int):
    cost = 0
    if 0 <= data:
        cost += 12000
    if 2 <= data:
        cost += 10000 * min((data - 1), 9) 
    if 10 < data:
        cost += 9000 * (data - 10)
    if 50 < data:
        cost *= 0.9
    return cost 

def write_data(filename:str, result:float):
    with open(filename, "w") as f:
        f.write(str(int(result)))

if __name__ == "__main__":
    data = read_data(filename='TAXI.INP')
    result = calculate(data=data)
    write_data(filename='TAXI.OUT', result=result)
    print('Lưu output thành công')
    
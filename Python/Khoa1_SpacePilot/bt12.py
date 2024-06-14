"""
Bài 1. 
Số hoàn hảo: là số mà tổng các ước số (không tính chính nó) của nó là 1 số bằng chính nó
Eg: số 6 thì có các ước là 1, 2, 3 và ta có 1 + 2 + 3 = 6 -> số 6 là 1 số hoàn hảo
Đề bài: Viết 1 hàm kiểm tra 1 số nhập vào từ bàn phím có phải là 1 số hoàn hảo không.
"""

def check_so_hoan_hao(number:int=None):
    if number == None:
        print('There is no number in input')
    # Thuật toán là tìm tất cả ước số (không tính number) của number, rồi cộng tổng nó lại, rồi so sánh với chính number
    sum_uoc_so = 0
    for i in range(1, number):
        if number % i == 0:
            sum_uoc_so += i
    return sum_uoc_so == number 

def test_bai_1():
    # Nhập 1 số từ bàn phím 
    input_data = input('Nhập vào 1 số để kiểm tra nó có phải số hoàn hảo không (nhập q để quit): ')
    while input_data != 'q':
        number = int(input_data) 
        print(f'{number} là số hoàn hảo:', check_so_hoan_hao(number=number))
        input_data = input('Nhập vào 1 số để kiểm tra nó có phải số hoàn hảo không (nhập q để quit): ')

"""
Bài 2. 
Nhập vào 1 số number và in ra các số hoàn hảo từ 1 đến number
"""
def print_nhung_so_hoan_hao(number:int=None):
    if number < 1 or number == None:
        print("number khong hop le")
    result = []
    for i in range(1, number + 1):
        if check_so_hoan_hao(i):
            result.append(i)
    return result

def test_bai_2():
    # Nhập 1 số từ bàn phím 
    input_data = input('Nhập vào 1 số để in ra các số hoàn hảo từ 1 đến nó (nhập q để quit): ')
    while input_data != 'q':
        number = int(input_data) 
        print(f'Các số hoàn hảo từ 1 đến {number}:', print_nhung_so_hoan_hao(number=number))
        input_data = input('Nhập vào 1 số để in ra các số hoàn hảo từ 1 đến nó (nhập q để quit): ')

if __name__ == "__main__":
    # test_bai_1()
    test_bai_2()


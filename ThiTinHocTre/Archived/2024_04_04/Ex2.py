def read_data():
    # n = int(input("Nhập giá trị n: "))
    array = list(map(int, input("Nhập giá trị các a_i: ").strip().split()))
    data = dict()
    for ele in array:
        if ele in data:
            data[ele] += 1
        else:
            data[ele] = 1
    return data


def process(data: dict) -> tuple:
    # from math import comb
    # comb(n, k) = n! / (k! * (n - k)!)

    raw = [(k, data[k]) for k in data if data[k] >= 4]
    max_length = sum([x[0] for x in raw])
    min_choice = min([x[1] for x in raw])
    return max_length**2, min_choice // 4


if __name__ == "__main__":
    '''
    Test 1: 7 5 3 2 3 6 3 3 -> 9 1
    Test 2: 3 3 3 3 3 3 1 1 1 1 6 6 6 6 6 -> 100 1
    '''
    data = read_data()
    result = process(data)
    print(result)

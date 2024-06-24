def read_data():
    n = int(input("Nhập giá trị n: "))
    data = list(map(int, input("Nhập giá trị các a_i: ").strip().split()))
    return n, data


def check(case: set, data: list) -> bool:
    for i in range(len(case) - 1):
        if (data[case[i]] + data[case[i + 1]]) % 2 == 0:
            return False
    return True


def process(n: int, data: list) -> int:
    from itertools import combinations

    index_data = range(n)
    all_possibility = []
    for k in range(2, n + 1):
        all_possibility += list(combinations(index_data, k))
    # print(all_possibility)
    count = 0
    for case in all_possibility:
        if check(case, data):
            # print('Accept', case)
            count += 1
        # else:
        #     print('Refuse', case)
    return count


if __name__ == "__main__":
    n, data = read_data()
    print(process(n, data))

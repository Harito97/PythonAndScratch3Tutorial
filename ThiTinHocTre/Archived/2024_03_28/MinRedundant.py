def read_input():
    n, s = map(int, input().split())
    data = list(map(int, input().split()))
    return n, s, data


def process(data: list, s: int):
    result = -1
    min_redundant = sum([record for record in data])
    MAX_RESULT_POSSIBLE = max(data)
    for i in range(1, MAX_RESULT_POSSIBLE + 1):
        total = sum([max(record - i, 0) for record in data])
        # print(f'min_redundant is {min_redundant}')
        # print(f'total is {total}')
        if s <= total < min_redundant:
            min_redundant = total
            result = i
    return result


if __name__ == "__main__":
    n, s, data = read_input()
    print(process(data=data, s=s))

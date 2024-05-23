import numpy as np


def get_input() -> np.array:
    m, n, w, h = map(int, input().strip().split())
    row = list(map(int, input().strip().split()))
    column = list(map(int, input().strip().split()))
    matrix = np.zeros((m, n))
    for i in range(m):
        for j in range(n):
            matrix[i][j] = row[i] + column[j]
    return matrix, m, n, w, h


def process(matrix: np.array, m: int, n: int, w: int, h: int):
    if w > n or h > m:
        return -1
    result_dict = dict()
    for i in range(m - h + 1):
        for j in range(n - w + 1):
            total = sum(sum(matrix[i : i + h, j : j + w]))
            # print(type(total))
            # print(total)
            if total in result_dict:
                result_dict[total] += 1
            else:
                result_dict[total] = 1
    max_key = max(result_dict, key=result_dict.get)
    return int(max_key), result_dict[max_key]


def main():
    """
    3 4 3 3
    1 -1 2
    2 2 2 2
    output: 24 2
    """
    matrix, m, n, w, h = get_input()
    print(process(matrix, m, n, w, h))


if __name__ == "__main__":
    main()

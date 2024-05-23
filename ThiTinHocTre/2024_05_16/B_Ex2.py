def read_input():
    n = int(input().strip())
    data = [int(input().strip()) for _ in range(n)]
    return data


def is_triangle(i, j, k):
    return i + j > k and j + k > i and k + i > j


def process(n: int, data: list[int]) -> int:
    count = 0
    for i in range(0, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if is_triangle(data[i], data[j], data[k]):
                    # print(data[i], data[j], data[k])
                    count += 1
    return count


def main():
    n = 5
    data = [6, 2, 4, 9, 3]
    print(process(n, data))


main()

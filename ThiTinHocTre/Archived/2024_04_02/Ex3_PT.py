n = int(input())
a = list(map(int, input().split()))


def longest_list(n: int, a: list):
    sum_list = 0
    max_len = 0
    max_start = 0
    for l in range(0, n):
        for r in range(n - 1, l, -1):
            sum_list = sum(a[l : r + 1])
            if sum_list > 0:
                length = r - l
                if length > max_len:
                    max_start = l
                    max_len = length
                elif length == max_len and l > max_start:
                        max_start = l
            sum_list = 0
    return max_start + 1, max_start + max_len + 1


print(longest_list(n, a))

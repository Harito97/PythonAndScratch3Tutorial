def double(n: int):
    if n == 0:
        return 1
    multiple = 1
    for i in range(n, 0, -2):
        multiple *= i
    if n % 2 == 0:
        multiple *= -1
    return multiple


def calculation(n: int):
    sum = 0
    for i in range(1, n + 1):
        sum += double(i)
    return sum


n = int(input())
print(calculation(n))

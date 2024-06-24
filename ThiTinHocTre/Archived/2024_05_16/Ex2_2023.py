def main():
    # n = int(input().strip())
    n = 9
    print(process(n))


def process(n: int) -> tuple:
    from math import gcd

    current = (1, n - 1)
    max_ucln = 1
    for a in range(2, n // 2):
        temp = gcd(a, n - a)
        if temp > max_ucln:
            max_ucln = temp
            current = (a, n - a)
    return current


main()

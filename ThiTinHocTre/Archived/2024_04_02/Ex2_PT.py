n = int(input())


def is_prime(n: int):
    if n >= 2:
        for i in range(2, int(n**0.5 + 1)):
            # use math.sqrt may faster than use ** 0.5
            if n % i == 0:
                return False
        return True
    return False


def prime_divisors(n: int):
    d = []
    if n >= 2:
        for i in range(2, n // 2 + 1):  # good
            if n % i == 0 and is_prime(i):
                d.append(i)
    return d


out = str(prime_divisors(n))
out = out.replace("[", "")
out = out.replace("]", "")
out = out.replace(",", "")
with open("NguyenTo.Out", "w") as fo:
    fo.write(str(out))

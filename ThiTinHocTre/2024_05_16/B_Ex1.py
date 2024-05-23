n = int(input().strip())
# u1 = 1, un = n
sum = n * (1 + n) / 2   # always integer as n or n + 1 % 2 == 0
print(int(sum))
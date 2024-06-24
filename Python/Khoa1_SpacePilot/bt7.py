# doc hieu lai code if-else cua bai 6 -> cach 1 va cach 2: sign * (-1)
# bai 7
# tinh 1 + 1 / 2 + 1 / 4 + 1 / 8 + 1 / 16 + ... + 1 / (2 ** n)
n = 100
result = 0
for i in range(n + 1):
    result += 1 / 2 ** i 
print('1 + 1 / 2 + 1 / 4 + 1 / 8 + 1 / 16 + ... + 1 / (2 ** ' + str(n) + ') =', result)
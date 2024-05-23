n = int(input())
cost = 0
if n > 0:
    cost += 15000
if 1 < n:
    cost += 13500 * min(4, n - 1)
if 5 < n:
    cost += 11000 * (n - 5)
if 100 < n:
    cost *= 0.9
print(cost)

# good
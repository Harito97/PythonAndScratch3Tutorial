a, b, c, d = map(int, input().split())
# 1 2 3 4
# input() -> '1 2 3 4' -> .split() -> ['1', '2', '3', '4'] -> map(int, array) -> a b c d = 1 2 3 4
count = 0
for x in range(a, b + 1):
    for y in range(c, d + 1):
        if x < y:
            count += 1
print(count)


# Goi y cach giam do phuc tap cua bai toan di
def function(a, b, c, d):
    if b <= a or d <= c:
        return None
    if d <= a:
        return 0
    if c < a:
        if d < b:
            return ...
        else:
            return ...
    else:  # c > a
        if d < b:
            return ...
        else:  # d >= b
            return (b - a + 1) * (d - c + 1)

# with open("PYTAGO.INP") as fi:
#     a, b = map(int, fi.readline().split())
# with open("PYTAGO.OUT", "w") as fo:
#     fo.write(str(int((a**2 + b**2) ** 0.5)))

from math import sqrt

# a, b = 3, 4
a, b = 6, 7
result = sqrt(a**2 + b**2)
if result - int(result) == 0:
    print(int(result))
else:
    print(round(result, 2))


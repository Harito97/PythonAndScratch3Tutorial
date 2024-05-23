from math import gcd

with open("COVID19.INP") as fi:
    n, m = map(int, fi.readline().split())
with open("COVID19.OUT", "w") as fo:
    ucln = gcd(n, m)
    fo.write(str(ucln) + "\n" + str(n // ucln) + " " + str(m // ucln))

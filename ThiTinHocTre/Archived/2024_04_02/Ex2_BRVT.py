with open("MAXCETRI.INP") as fi:
    n = int(fi.readline())
    a = [int(i) for i in fi.readlines()]


def calculate(a: list):
    max_a = max(a)
    
    while a.count(max_a) < 3:
        # remove all item have good length but haven't enough 3 to create a triangle 
        a.remove(max_a)
        max_a = max(a)
    
    k = a.count(max_a)
    ans = ((k - 2) * (k - 1) * k) // 6
    return ans


with open("MAXCETRI.OUT", "w") as fo:
    fo.write(str(calculate(n, a)))

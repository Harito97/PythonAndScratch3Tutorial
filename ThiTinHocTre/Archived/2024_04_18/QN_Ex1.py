# from itertools import combinations

# with open("CHIAQUA.INP") as fi:
#     n = int(fi.readline())
#     a = list(map(int, fi.readline().split()))


# def check(a):
#     a_temp = a.copy()
#     for i in range(1, len(a)):
#         for combo in combinations(a, i):
#             for i in range(len(combo)):
#                 a.remove(combo[i])
#             if sum(combo) == sum(a):
#                 return "YES"
#             a = a_temp.copy()
#     return "NO"


# with open("CHIAQUA.OUT", "w") as fo:
#     fo.write(str(check(a)))

def check(a:list[int]) -> str:
    # a contains only 100 or 200
    half = sum(a) / 2
    return half % 100 == 0

a = [100, 200, 100]
# a = [100, 100, 100, 200]
a = [100, 100, 100, 200, 100]
print(check(a))
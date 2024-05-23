# with open("CODE.INP") as fi:
#     n = int(fi.readline())
#     a = [int(i) for i in fi.readlines()]


# def find(a):
#     for i in range(max(a), min(a) - 1, -1):   # O(n ** 3)
#         if i not in a:
#             return i
#     return min(a) - 1


# with open("CODE.OUT", "w") as fo:
#     fo.write(str(find(a)))

def process(a:list[int])->int:
    if len(a) > len(set(a)):
        return -1
    a.sort(reverse=True)    # O(n * log(n))
    for i in range(len(a) - 1): # O(n)
        if a[i] - 1 > a[i + 1]:
            return a[i] - 1
    return a[0] + 1

# a = [7, 4, 2, 6, 1, 3]    # 5
a = [7, 4, 2, 6, 1, 3, 5]   # 8
print(process(a))
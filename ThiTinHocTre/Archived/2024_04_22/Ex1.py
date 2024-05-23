# with open("CAU1.INP") as fi:
#     n = int(fi.readline())
#     a = list(map(int, fi.readline().split()))
# a_temp = a.copy()
# i = 0
# count = 0
# lst = []
# while i != n - 1:
#     le = False
#     schan = 0
#     sle = 0
#     for _ in range(len(a)):
#         if _ != i:
#             if le == False:
#                 sle += a[i]
#                 le = True
#             else:
#                 schan += a[i]
#                 le = False
#     if schan == sle and a[i] not in lst:
#         count += 1
#         lst.append(a[i])
#     i += 1
# with open("CAU1.OUT", "w") as fo:
#     fo.write(str(count))


def process(array: list[int]):
    result = 0
    for i in range(len(array)):
        if i % 2 == 0:
            sum_even = sum(array[j] for j in range(0, i, 2)) + sum(
                array[j] for j in range(i + 2, len(array), 2)
            )
            sum_odd = sum(array[j] for j in range(1, i, 2)) + sum(
                array[j] for j in range(i + 1, len(array), 2)
            )
        else:
            sum_even = sum(array[j] for j in range(0, i, 2)) + sum(
                array[j] for j in range(i + 1, len(array), 2)
            )
            sum_odd = sum(array[j] for j in range(1, i, 2)) + sum(
                array[j] for j in range(i + 2, len(array), 2)
            )
        if sum_even == sum_odd:
            result += 1
    return result


def main():
    a = [7, 7, 6, 7, 7, 7, 8]
    print(process(a))


main()

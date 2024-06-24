def read_input():
    n, k = map(int, input().strip().split())
    data = [int(input().strip()) for _ in range(n - 1)]
    return n, k, data


def read_input_test():
    str_input = "7 3"
    n, k = map(int, str_input.strip().split())
    str_input = "2 2 2 3 2 2"
    data = list(map(int, str_input.strip().split()))
    return n, k, data


# def process(n: int, k: int, data: list[int]) -> int:
#     data = [10**6 + 1] + data + [10**6 + 1]
#     up_flag = [False] * (len(data) + 1)
#     up_flag[0], up_flag[k], up_flag[-1] = True, True, True
#     down_flag = up_flag[:]
#     up_price, down_price = 0, 0
#     up_price_up, up_price_down = 0, 0
#     down_price_up, down_price_down = 0, 0
#     print(data, up_flag, down_flag, sep="\n")
#     for i in range(1, k + 1):
#         print("Chieu up:", i)
#         # up tien
#         if not up_flag[i]:
#             if data[i] < data[i + 1]:
#                 up_price_up += data[i]
#                 up_flag[i - 1], up_flag[i] = True, True
#             else:
#                 up_price_up += data[i + 1]
#                 up_flag[i], up_flag[i + 1] = True, True
#         # up lui
#         if not down_flag[k - i]:
#             if data[k - i] < data[k - i + 1]:
#                 up_price_down += data[k - i]
#                 down_flag[k - i - 1], down_flag[k - i] = True, True
#             else:
#                 up_price_down += data[k - i + 1]
#                 down_flag[k - i], down_flag[k - i + 1] = True, True
#         print(up_flag, down_flag, up_price_up, up_price_down)
#     up_price = min(up_price_up, up_price_down)
#     for i in range(k + 1, n):
#         print("Chieu down:", i)
#         # down tien
#         if not up_flag[i]:
#             if data[i] < data[i + 1]:
#                 down_price_up += data[i]
#                 up_flag[i - 1], up_flag[i] = True, True
#             else:
#                 down_price_up += data[i + 1]
#                 up_flag[i], up_flag[i + 1] = True, True
#         # down lui
#         down_index = n + k + 1 - i
#         print(down_index)
#         if down_index == n and not down_flag[down_index]:
#             down_price_down += data[down_index - 1]
#             down_flag[down_index - 1], down_flag[down_index] = True, True
#             continue
#         if not down_flag[down_index]:
#             if data[down_index] < data[down_index + 1]:
#                 down_price_down += data[down_index]
#                 down_flag[down_index - 1], down_flag[down_index] = True, True
#             else:
#                 down_price_down += data[down_index + 1]
#                 down_flag[down_index], down_flag[down_index + 1] = True, True
#         print(up_flag, down_flag, down_price_up, down_price_down)
#     down_price = min(down_price_up, down_price_down)
#     return up_price + down_price


# def process(n: int, k: int, data: list[int]) -> int:
#     ele_needed = [1, n - 1]
#     ele_no_needed = [k - 1, k]
#     data = [-1] + data
#     all_possible = []
#     for i in range(n // 2):
#         ...
#         # dùng giải thuật vét cạn lấy mọi trường hợp: i là số cạnh liên kết bỏ

def process(n, k, data):
    unnecessary = [k - 1, k - 2]
    unnecessary = set([max(0, x) for x in unnecessary])
    i = 0
    while i in unnecessary:
        i += 1
    necessary = [i]
    i = n - 2
    while i in unnecessary:
        i -= 1
    # if i in range(n - 1):
    #     necessary.append(i)
    necessary.append(i)
    print(necessary, unnecessary)
    # temp = set()
    # for ele in unnecessary:
    #     print(ele, ele + 1, ele - 1)
    #     if ele + 1 in range(n + 1) and ele + 1 not in necessary:
    #         temp.add(ele + 1)
    # unnecessary.update(temp)
    # print(necessary, unnecessary)
    price = sum(data[ele] for ele in necessary)
    print(price)
    not_yet = [i for i in range(1, n - 1) if i not in unnecessary and i not in necessary]
    print(not_yet)
    yet = set()
    for index in necessary:
        yet.add(index)
        yet.add(index + 1)
    while len(not_yet) != 0:
        min_index = max(not_yet, key=lambda index: data[index])
        # if min_index in range(n - 1):
        yet.add(min_index)
        yet.add(min_index + 1)
        price += data[min_index]
        not_yet.remove(min_index)
        # not_yet = [i for i in not_yet if i not in unnecessary and i not in necessary]
        print(not_yet, yet)
    return price



def main():
    n, k, data = read_input_test()
    print(n, k, data)
    print(process(n, k, data))


if __name__ == "__main__":
    main()

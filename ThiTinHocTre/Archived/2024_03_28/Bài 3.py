# n=int(input())
# danhsach=[]
# for i in range(n):
#     a,b,c=map(int,input().split())
#     danhsach.append((a,b,c))
# def tiennhieunhat(n:int,danhsach:list):
#     danhsach.sort(key=lambda x:x[0])

# em cần có giải thuật đúng trước khi giải đã


def is_overlap(data1: list, data2: list):
    return data1[0] <= data2[0] <= data1[1] or data2[0] <= data1[0] <= data2[1]
    # return data1[0] <= data2[0] < data1[1] or data2[0] <= data1[0] < data2[1]


def find_all_possibility(data: list):
    count = 1
    data.sort(key=lambda x: (x[0], x[1]))
    # print(data)
    result = []
    for record in data:
        # print(f'result is {result}')
        added = False
        for ele in result:
            if not is_overlap(ele[-1], record):
                ele.append(record)
                added = True
        if not added:
            for ele in result:
                for i in range(len(ele) - 1, -1, -1):
                    if count >= 100:
                        return result
                    count += 1
                    # print(f'result is {result}')
                    if is_overlap(ele[i], record):
                        # print(f'{ele[i]} bi trung lap voi {record}')
                        continue
                    else:
                        # print(f'{ele[i]} khong trung voi {record}')
                        result.append(ele[:i] + [ele[i], record])
                        added = True
                        break
                if added:
                    break
            else:
                # print(f'{record} duoc them moi vao result')
                result.append([record])
    return result


def find_max(data: list):
    # data is a 2D array
    max_profit = 0
    for case in data:
        total_profit = sum([a[2] for a in case])
        if max_profit < total_profit:
            max_profit = total_profit
    return max_profit


if __name__ == "__main__":
    n = int(input())
    orders = [list(map(int, input().split())) for i in range(n)]
    result = find_all_possibility(data=orders)
    print(find_max(data=result))

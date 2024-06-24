def read_input():
    n, k = map(int, input().split())
    data = list(map(int, input().split()))
    return n, k, data


def process(k, data):
    from itertools import combinations
    all_possibility = combinations(data, k)

    value_order = dict()
    for index, item in enumerate(data):
        if item in value_order:
            value_order[item].append(index)
        else:
            value_order[item] = [index]
            
    data = sorted(data, reverse=True)
    MAX_ = sum(data[:k])
    # print('value_order =', value_order)
    total = 0
    for case in all_possibility:
        if total == MAX_:
            # soon end
            break
        # print('case =', case)
        temp = []
        for ele in case:
            temp.append(value_order[ele])  
        # print('temp =', temp)
        for i in range(k - 1):
            if temp[i][0] >= temp[i + 1][0] or case[i] >= case[i + 1]:
                break
        else:
            sum_ = sum(case)
            total = max(total, sum_)
    
    print(total)


if __name__ == "__main__":
    # Test 1
    k = 3
    data = [10, 5, 7, 8, 8, 2, 9, 3, 11]

    # # Test 2
    # n, k, data = read_input()
    
    # # Test 3
    # k = 2
    # data = [2, 4, 7, 5, 9]
    
    process(k, data)


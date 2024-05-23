# n,g=map(int,input().split())
# c=list(map(int,input().split()))
# count=0
# for group_i in range(g):
#     group=list(set(c))
#     for i in range(len(group)):
#         c.remove(group[i])
#     count+=len(group)
# print(count)

# ?? code như trên không đúng giải thuật

n, g = map(int, input().split())
c = list(map(int, input().split()))


def divide_array(array, k, n):
    # n = len(array)
    result = []

    def backtrack(start, current_partition):
        if start == n:
            if len(current_partition) == k:
                result.append(current_partition[:])
            return
        for end in range(start + 1, n + 1):
            current_partition.append(array[start:end])
            backtrack(end, current_partition)
            current_partition.pop()

    backtrack(0, [])
    return result


def find_max(partitions: list, array):
    MAX_POSSIBLE = len(set(array))
    max_diversity = 0
    for partition in partitions:
        temp = sum([len(set(ele)) for ele in partition])
        if max_diversity < temp:
            max_diversity = temp
        if max_diversity >= MAX_POSSIBLE:
            break  # soon end
    return max_diversity


result = divide_array(array=c, k=g, n=n)
print(find_max(partitions=result, array=c))

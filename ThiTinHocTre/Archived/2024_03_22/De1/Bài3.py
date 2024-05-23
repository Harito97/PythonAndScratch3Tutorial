from itertools import combinations

n = int(input())
a = list(map(int, input().split()))
a_temp = a.copy() # a[:]
min_difference = None
for i in range(1, n + 1):
    for combo in combinations(a, i):
        for j in range(i):
            a.remove(combo[j])
        if min_difference == None or abs(sum(a) - sum(combo)) < min_difference:
            min_difference = abs(sum(a) - sum(combo))
            first_list = list(combo) # [int(combo[i]) for i in range(len(combo))]
            second_list = a
        # a.clear()
        a = a_temp.copy()

if sum(first_list) > sum(second_list):
    print(second_list)
    print(first_list)
else:
    print(first_list)
    print(second_list)


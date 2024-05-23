# n = int(input())
# h = list(map(int, input().split()))
# max_list = []
# max_count = 0
# for i in range(n):
#     if h.count(h[i]) > max_count:
#         max_count = h.count(h[i])
#         max_list.clear()
#         max_list.append(h[i])
#         max_list.append(h.count(h[i]))
# print(max_list)

# em co the dung dictionary cho ngan gon hon


n = int(input())
h = list(map(int, input().split()))

data = dict()
for student in h:
    if student not in data:
        data[student] = 1
    else:
        data[student] += 1

inverse = [(value, key) for key, value in data.items()]
# print(max(inverse)[1])
print(max(data, key=data.get))
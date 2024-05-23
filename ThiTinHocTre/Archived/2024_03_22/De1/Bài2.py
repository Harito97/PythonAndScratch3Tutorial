possible_answers = []

a, b, c, d = map(int, input().split())

for i in range(4):
    answer = (a / c) + (b / d)
    possible_answers.append(answer)
    a, b, c, d = c, a, d, b
    # d_temp = d
    # d = a
    # a = b
    # b = c
    # c = d_temp

print(possible_answers.index(max(possible_answers)))

a = [1, 5]
m = 5
count = 0
for i in a:
    for j in a:
        for k in a:
            if i * j * k % 5 == 0:
                count += 1
print(count)
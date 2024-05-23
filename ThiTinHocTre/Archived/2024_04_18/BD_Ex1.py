# output can only be -1 1 or 2
# (m, n) = {(0, 0), (0, 1), (1, 0), (1, 1)}
a = 'helloworld'
b = 'oworldhell'
# b = 'helloworld'
# b = 'oworldhelledf'
m, n = 0, 0

for i in range(0, len(a)):
    prefix = b[:i]
    suffix = b[i:]
    if suffix + prefix == a:
        if len(prefix) == 0:
            m, n = 0, 1
        elif len(suffix) == 0:
            m, n = 1, 0
        else:
            m, n = 1, 1
        break

result = m + n
if result == 0:
    print('-1')
else:
    print(result)

def process(st):
    max_len = 0
    for l in range(len(st)):
        for r in range(len(st) - 1, l, -1):
            s = st[l:r + 1]
            if s[::-1] == s and len(s) > max_len:
                max_len = len(s)
            if max_len == len(st):
                # end soon
                return max_len
    return max_len

st = 'abfghiklmlkihgh'
print(process(st))

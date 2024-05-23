s = input().upper()
score = 0
count = 0
for i in range(len(s)):
    if s[i] == "Y":
        count += 1
        score += count
    elif s[i] == "N":
        count = 0
print(score)

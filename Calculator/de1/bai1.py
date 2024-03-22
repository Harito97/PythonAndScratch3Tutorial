number = input()

while number[::-1] != number:
    new_number = int(number) + int(number[::-1])
    number = str(new_number)

print(number)
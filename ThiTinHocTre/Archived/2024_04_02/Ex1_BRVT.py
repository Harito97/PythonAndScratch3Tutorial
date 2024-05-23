with open("EMPTHOLE.INP") as f:
    n = f.readline()


def calculate(number: str):
    holes = 0
    one = ['0', '4', '6', '9']
    two = ['8']
    for character in number:
        if character in one:
            holes += 1
        elif character in two:
            holes += 2
    return str(holes)


with open("EMPTHOLE.OUT", "w") as f:
    f.write(calculate(n))

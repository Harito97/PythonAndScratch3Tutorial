def read_input():
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    return n, a

def read_input_test():
    # n = 9
    # data =  '1 2 3 4 5 6 7 8 9'
    n = 8
    data = '1 -1 1 -1 1 -1 1 -1'
    a = list(map(int, data.strip().split()))
    return n, a

def process(a:list[int]):
    a = [0] + a
    output = []
    for x in range(1, len(a)):
        count = 0
        for i in range(1, x - 2):
            for j in range(i + 1, x - 1):
                for k in range(j + 1, x):
                    if a[i] + a[j] + a[k] == a[x]:
                        # print(a[i], a[j], a[k], '=', a[x])
                        count += 1
        output.append(count)
    return output[1:]

def main():
    n, a = read_input_test()
    print(process(a))

if __name__ == "__main__":
    main()

def read_input() -> tuple[int, list]:
    n = int(input().strip())
    data = list(map(int, input().strip().split()))
    return n, data

def process(n:int, data:list[int]) -> int:
    data.sort(reverse=True)
    result = 0
    for i in range(n):
        collect = data[i] - i
        if collect <= 0:
            break
        result += collect
    return result

def main():
    n, data = read_input()
    print(process(n, data))

if __name__ == "__main__":
    """
    4 
    3 3 3 3

    4 
    3 1 4 3
    """
    main()
    
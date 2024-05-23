def read_input():
    n = int(input().strip())
    k = int(input().strip())
    data = []
    for i in range(k):
        record = tuple(map(int, input().strip().split()))
        data.append(record)
    return n, data 

def count_tin(n: int, state:list[int]):
    count = 0
    for i in range(1, n + 1):
        if state[i] == 0:
            # la Tin
            count += 1
    return count

def process(n:int, data:list[tuple]) -> list:
    result = []
    state = [-1] * (2 * n + 1)  
    for i in range(1, n + 1):
        state[i] = 0
        state[i + n] = 1
        # state[0] = -1
    for ele in data:
        state[ele[0]], state[ele[1]] = state[ele[1]], state[ele[0]] # swap
        result.append(count_tin(n, state))
    return result

def process(n:int, data:list[tuple]) -> list:
    result = ''
    state = [-1] * (2 * n + 1)  
    count = n
    for i in range(1, n + 1):
        state[i] = 0
        state[i + n] = 1
        # state[0] = -1
    for ele in data:
        print(state)
        print(ele)
        if ele[1] > n and ele[0] <= n:
            if state[ele[1]] == 1 and state[ele[0]] == 0:
                count -= 1
            elif state[ele[1]] == 0 and state[ele[0]] == 1:
                count += 1
        state[ele[0]], state[ele[1]] = state[ele[1]], state[ele[0]] # swap
        # result.append(count_tin(n, state))
        result += str(count) + '\n'
    return result

def main():
    """
    2
    4
    1 3
    3 4
    4 1
    2 3
    """
    n, data = read_input()
    print(process(n, data))

if __name__ == "__main__":
    main()
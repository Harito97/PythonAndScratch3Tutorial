def read_input():
    n, k = map(int, input().strip().split())
    data = dict()
    for _ in range(k):
        temp = list(map(int, input().strip().split()))
        data[(temp[0], temp[1])] = temp[2]
    return n, data


def find_all_horse_path(coordinate: tuple, n: int):
    data = [
        (coordinate[0] - 1, coordinate[1] - 2),
        (coordinate[0] - 2, coordinate[1] - 1),
        (coordinate[0] + 1, coordinate[1] - 2),
        (coordinate[0] + 2, coordinate[1] - 1),
        (coordinate[0] + 1, coordinate[1] + 2),
        (coordinate[0] + 2, coordinate[1] + 1),
        (coordinate[0] - 1, coordinate[1] + 2),
        (coordinate[0] - 2, coordinate[1] + 1),
    ]

    return [case for case in data if 1 <= case[0] <= n and 1 <= case[1] <= n]

def process(n:int, data:dict):
    common_dict = dict()
    for record in data.keys():
        common_dict[record] = find_all_horse_path(record, n)
    # print(f"Common_dict: {common_dict}")
    reward_dict = dict()
    for reward, all_path in common_dict.items():
        for path in all_path:
            if path in reward_dict:
                reward_dict[path] += data[reward]
            else:
                reward_dict[path] = data[reward]
    # print(f"Reward dict: {reward_dict}")
    return max(reward_dict.values())

if __name__ == "__main__":
    """
    Test 0:
    5 4
    5 1 3
    4 4 5
    2 5 1
    1 4 6
    """
    n, data = read_input()
    print(process(n, data))
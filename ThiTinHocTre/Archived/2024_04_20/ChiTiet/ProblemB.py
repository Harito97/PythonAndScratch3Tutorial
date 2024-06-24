def input():
    n = ...
    k = 4
    raw_data = [8, 7, 5, 4, 8, 4]
    clean_data = dict()
    for i in range(len(raw_data)):
        if raw_data[i] in clean_data:
            clean_data[raw_data[i]].append(i)
        else:
            clean_data[raw_data[i]] = [i]
    return k, clean_data


def check(k: int, array: list[int]):
    for i in range(len(array) - 1):
        if (
            array[i + 1] - array[i] <= k
        ):  # vì thực hiện clean_data đã đảm bảo array tăng dần
            return True
    return False


def process(k: int, clean_data: dict):
    # Lọc các phần tử có độ dài của mảng value lớn hơn hoặc bằng 2
    filtered_data = {key: value for key, value in clean_data.items() if len(value) >= 2}
    lucky_numbers = []
    for key, value in clean_data.items():
        if check(k ,value):
            lucky_numbers.append(key)
    if len(lucky_numbers) == 0:
        return -1
    lucky_number = max(lucky_numbers)
    return lucky_number, len(filtered_data[lucky_number])


def main():
    k, clean_data = input()
    print(process(k, clean_data))


main()

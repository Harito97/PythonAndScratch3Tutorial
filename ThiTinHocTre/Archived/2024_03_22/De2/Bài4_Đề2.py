def read_data_and_calculate(filename: str):
    with open(filename) as f:
        num_user = int(f.readline().strip())
        num_bike = num_user
        data = []
        for i in range(num_user):
            data.append(list(map(int, f.readline().strip().split())))
        data.sort(key=lambda x: (x[0], x[1]))
    for i in range(num_user - 1):
        for j in range(i + 1, num_user):
            if not is_overlap(data[i], data[j]):
                num_bike -= 1
                break
    return num_bike


def is_overlap(data1: list, data2: list):
    # return data1[0] <= data2[0] <= data1[1] or data2[0] <= data1[0] <= data2[1]
    return data1[0] <= data2[0] < data1[1] or data2[0] <= data1[0] < data2[1]


def write_data(filename: str, result: float):
    with open(filename, "w") as f:
        f.write(str(int(result)))


if __name__ == "__main__":
    data = read_data_and_calculate(filename="BIKE.INP")
    write_data(filename="BIKE.OUT", result=data)
    print("Lưu output thành công")

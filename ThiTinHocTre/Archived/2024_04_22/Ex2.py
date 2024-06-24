import timeit
from itertools import combinations


def get_input():
    n = int(input().strip())
    data = []
    for _ in range(n):
        point = tuple(map(int, input().strip().split()))
        data.append(point)
    return data


def check(quadrangle):
    # Kiểm tra quadrangle có phải là hình chữ nhật hay không
    x_coords = [point[0] for point in quadrangle]
    y_coords = [point[1] for point in quadrangle]
    return len(set(x_coords)) == 2 and len(set(y_coords)) == 2


def process_with_combinations(data):
    all_quadrangles = combinations(data, 4)
    result = sum(check(quadrangle) for quadrangle in all_quadrangles)
    return result


def process_with_loops(data):
    all_quadrangles = []
    for i in range(len(data) - 3):
        for j in range(i + 1, len(data) - 2):
            for k in range(j + 1, len(data) - 1):
                for l in range(k + 1, len(data)):
                    quadrangle = [data[i], data[j], data[k], data[l]]
                    all_quadrangles.append(quadrangle)
    result = sum(check(quadrangle) for quadrangle in all_quadrangles)
    return result


def main():
    """
    input example:
    6
    1 4
    3 4
    5 4
    1 1
    3 1
    5 1
    result: 3
    """
    data = get_input()

    print(process_with_combinations(data))
    # time_combinations = timeit.timeit(
    #     lambda: process_with_combinations(data),
    #     number=1000
    # )
    # print("Time with combinations:", time_combinations)

    # time_loops = timeit.timeit(
    #     lambda: process_with_loops(data),
    #     number=1000
    # )
    # print("Time with loops:", time_loops)


if __name__ == "__main__":
    main()
    # Thử nghiệm thấy dùng các vòng for cho kết quả nhanh gấp 3
    # Time with combinations: 0.09241902500070864
    # Time with loops: 0.037571052998828236

def find_largest_subgrid(matrix, k):
    m = len(matrix)
    n = len(matrix[0])

    max_subgrid_size = 0

    # Tính prefix sums để có thể tính số lượng kí tự 'A' và 'B' trong một phạm vi nhanh chóng
    prefix_sums = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            prefix_sums[i][j] = prefix_sums[i - 1][j] + prefix_sums[i][j - 1] - prefix_sums[i - 1][j - 1] + (matrix[i - 1][j - 1] == 'A')

    # Kiểm tra tất cả các hình chữ nhật con có thể
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            for p in range(i, m + 1):
                for q in range(j, n + 1):
                    num_A = prefix_sums[p][q] - prefix_sums[p][j - 1] - prefix_sums[i - 1][q] + prefix_sums[i - 1][j - 1]
                    num_B = (p - i + 1) * (q - j + 1) - num_A
                    if abs(num_A - num_B) <= k:
                        max_subgrid_size = max(max_subgrid_size, (p - i + 1) * (q - j + 1))

    return max_subgrid_size


def main():
    T = int(input().strip())
    result = []
    for _ in range(T):
        m, n, k = map(int, input().strip().split())
        matrix = [input().strip() for _ in range(m)]

        result.append(find_largest_subgrid(matrix, k)) 
    for x in result:
        print(x)


if __name__ == "__main__":
    main()

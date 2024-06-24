def longestIncreasingSubsequence(arr):
    n = len(arr)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


def process(arr):
    return len(arr) - longestIncreasingSubsequence(arr)


def main():
    A = [6, 7, 5, 5, 4, 5]  # 4
    A = [6, 7, 5, 5, 4, 5, 3]  # 5
    print(process(A))


main()

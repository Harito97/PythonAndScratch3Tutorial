def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_longest_subarray(arr):
    n = len(arr)
    max_len = 0
    l = 0

    for i in range(n - 1):
        d = arr[i]
        for j in range(i + 1, n):
            d = gcd(d, arr[j])
            if d == 1:
                break
            l += 1
            max_len = max(max_len, l)
        l = 0
    
    return max_len + 1

# Example usage
arr = [2, 4, 6, 8, 10, 12, 14]
arr = [1, 2, 3]
# arr = [2, 6, 12, 15, 27, 1, 81, 5]
# arr = [11, 2, 4, 6, 8, 10, 12]
# arr = [2, 4, 6, 8, 10, 12, 14]
print("Độ dài dãy liên tiếp dài nhất là:", find_longest_subarray(arr))

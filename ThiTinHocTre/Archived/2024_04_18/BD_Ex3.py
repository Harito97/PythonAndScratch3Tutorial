# with open("CAU3.INP") as fi:
#     n = int(fi.readline())
#     a = list(map(int, fi.readline().split()))


# def solve(arr):
#     if not arr:
#         return 0
#     n = len(arr)
#     max_length = 1
#     current_length = 1
#     for i in range(1, n):
#         if arr[i] > arr[i - 1]:
#             current_length += 1
#         else:
#             max_length = max(max_length, current_length)
#             current_length = 1
#     max_length = max(max_length, current_length)
#     return max_length


def get_subarrays(arr):
    subarrays = []
    n = len(arr)
    # Duyệt qua tất cả các vị trí bắt đầu
    for start in range(n):
        # Duyệt qua tất cả các vị trí kết thúc
        for end in range(start + 1, n + 1):
            # Lấy ra mảng con từ vị trí bắt đầu đến vị trí kết thúc
            subarray = arr[start:end]
            subarrays.append(subarray)
    return subarrays


def check_increasing(arr):
    # Duyệt qua từng phần tử trong mảng
    for i in range(1, len(arr)):
        # Nếu có một phần tử nhỏ hơn hoặc bằng phần tử trước đó
        # thì mảng không tăng dần
        if arr[i] <= arr[i - 1]:
            return False
    # Nếu không tìm thấy phần tử nào không thỏa mãn điều kiện
    # thì mảng tăng dần
    return True


def process(a: list[int]):
    max_length = 0
    for i in range(len(a)):
        b = a.copy()
        b.remove(a[i])
        # print(b)
        all_subarrays = get_subarrays(b)
        for sub in all_subarrays:
            if check_increasing(sub) and max_length < len(sub):
                max_length = len(sub)
                if len(sub) == len(a):
                    # soon end
                    return max_length
    return max_length


# a = [2, 4, 1, 5, 7, 3]    # 4
a = [2, 4, 1, 5, 7, 9, 11, 3]  # 6
print(process(a))

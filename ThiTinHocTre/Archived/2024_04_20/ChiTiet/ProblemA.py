def input():
    N = ...
    data = [16, 17, 4, 3, 5, 2, 7]  # [17, 7]
    data = [16, 17, 4, 3, 5, 2]  # [17, 5, 2]
    return data

def process(data:list[int]):
    # result = [[data[0]]]
    result = [data[0]]
    # max_result = data[0]
    max_result = result[-1]
    final_result = []
    for i in range(1, len(data)):
        max_data = max(data[i:])    # có thể thêm thủ thuật ở đây để tính max_data 1 cách nhanh hơn việc dùng max(data[i:]) tuy nhiên đánh đổi là code dài hơn và tốn bộ nhớ hơn
        if max_data > max_result:
            # result[-1].append(data[i])
            if data[i] > max_result:
                result[-1] = data[i]
                max_result = data[i]
        else:
            # result.append([data[i]])
            result.append(data[i])
            max_result = data[i]
    # ở đây result có 2 cách biểu diễn 
    # cách 1 là 1 mảng 2D -> dễ hiểu theo logic chuyển mọi phần tử từ data sang result -> tốn bộ nhớ và không cần thiết cho kết quả cuối cùng
    # cách 2 là 1 mảng 1D chỉ lưu lại giá trị max của mỗi phân đoạn -> chính là kết quả cuối cùng
    # nếu dùng cách biểu diễn 1 thì cần tạo thêm 1 mảng 1D nữa duyệt qua mảng result để lấy ra phần tử đuôi - cũng là phần tử max của mỗi phân đoạn
    # ngoài ra có thể thay thế biến max_result = result[-1] luôn (với cách biểu diễn result là mảng 1D) cho tiết kiệm bộ nhớ nhưng thầy giữ lại biến này để em đọc hiểu code
    return result

def main():
    data = input()
    print(process(data))

main()        
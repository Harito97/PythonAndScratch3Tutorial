"""
Chắc hẳn các bạn học sinh chúng ta ai cũng biết bài toán cổ về bàn cờ vua và hạt thóc. 
Và hôm nay các bạn sẽ được làm quen với một biến thể của nó: 
Cho một dãy ô vuông được đánh thứ tự từ trái qua phải là những số nguyên dương liên tiếp từ a tới b. 
Ô vuông đầu tiên có 2 ** a hạt thóc, các ô vuông tiếp theo mỗi ô vuông có số hạt thóc gấp đôi ô vuông đứng liền kề trước nó.
Yêu cầu: Tính xem tổng số hạt thóc trong các ô vuông chia cho 127 sẽ dư bao nhiêu trong thời gian nhanh nhất có thể.
Dữ liệu vào: đọc từ file MATHS.INP gồm:
Dòng thứ nhất là số nguyên dương a(a <= 10**18)
Dòng thứ hai là số nguyên dương b(b <= 10**18)
"""

def process(a: int, b: int):
    total = 0
    for i in range(a, b + 1):
        total += 2**i % 127
    return total % 127

a, b = 1, 90000
print(process(a, b))
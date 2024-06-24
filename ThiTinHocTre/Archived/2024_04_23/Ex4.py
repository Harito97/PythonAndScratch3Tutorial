def get_input():
    text = input() + ' '    # phòng trường hợp char ở vị trí cuối cùng là sô thì nó cũng thêm vào
    data = []
    current = ""
    for char in text:
        if char.isdigit():
            current += char
        elif current != '':
            data.append(current)
            current = ""
    return data


def get_all_num(data: list[str]):
    # all_num = set()
    all_num = []
    for ele in data:
        for i in range(len(ele)):
            for j in range(i + 1, len(ele) + 1):
                # all_num.add(int(ele[i:j]))
                all_num.append(int(ele[i:j]))   # vì cái thứ tự in output là 2 23 3 5 rất ngớ ngẩn
    return all_num


def check_prime(num: int):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def process(all_num: set[int]):
    result = [] # giả sử trong all_num có 2 giá trị a, b | a == b và a là số nguyên tố thì in ra kiểu gì ??
    for num in all_num:
        if num in result:
            continue
        if check_prime(num):
            result.append(num)
    return len(result), result

def main():
    data = get_input()
    print(data)
    all_num = get_all_num(data)
    print(all_num)
    print(process(all_num))

if __name__ == "__main__":
    """ 
    Test1#2primary9#5key6

    Test1234#primarykey542
    """
    main()

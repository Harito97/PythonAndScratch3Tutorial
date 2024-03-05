# tinh giai thua

def tinh_giai_thua(number:int):
    if number < 0:
        return -1
    elif number == 0:
        return 1
    result = 1
    # ...
    return result

if __name__ == "__main__":
    number = int(input())
    print(tinh_giai_thua(number=number))
    
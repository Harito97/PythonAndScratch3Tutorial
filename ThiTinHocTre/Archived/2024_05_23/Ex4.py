# origin_money = 125
origin_money = 5
# k = 6
array = [1,2,5,10,20,50]
array = [2,4,6]

def process(origin_money:int, array:list):
    array.sort(reverse=True)
    result = 0
    min_money = min(array[1:])
    for money in array:
        if origin_money < money:
            # print('Skip', money)
            continue
        result += origin_money // money
        residual = origin_money % money
        # print(result, residual)
        for i in array[1:]:
            if residual < min_money:
                return -1
            if residual < i:
                continue
            result += residual // i
            residual = residual % i
        if residual == 0:
            return result
    return -1
    
print(process(origin_money, array))
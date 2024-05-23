# base=input()
# goal=input()
# count=0
# num='0123456789'
# for i in range(len(base)):
#     have=int(base[i]);need=int(goal[i])
#     if need>have:
#         best_option=need-have
#         if (have+10)-need<best_option:
#             best_option=(have+10)-need
#     else:
#         best_option=have-need
#         if (need+10)-have>best_option:
#             best_option=(need+10)-have
#     count+=best_option
# print(count)

def read_data_and_calculate(filename:str):
    with open(filename) as f:
        current = f.readline()
        password = f.readline()
        need_times = 0
        # xoay tối đa từ 1 đến 5 là max 
        for char_current, char_password in zip(current, password):
            temp = abs(int(char_current) - int(char_password))
            need_times += min(temp, 10 - temp)
    return need_times

def write_data(filename:str, result:float):
    with open(filename, "w") as f:
        f.write(str(int(result)))

if __name__ == "__main__":
    data = read_data_and_calculate(filename='LOCK.INP')
    write_data(filename='LOCK.OUT', result=data)
    print('Lưu output thành công')
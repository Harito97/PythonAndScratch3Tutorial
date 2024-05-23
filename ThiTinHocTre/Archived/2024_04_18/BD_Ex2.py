# # def calculate(times: list):
# #     hour = ""
# #     minute = ""
# #     if 2 in times:
# #         _ = list(filter(lambda x: x <= 3, times))
# #         if len(_) > 0:
# #             hour += "2"
# #             hour += str(max(_))
# #             times.remove(2)
# #             times.remove(max(_))
# #             for i in range(2):
# #                 if i == 0:
# #                     chose_one = max(list(filter(lambda x: x <= 6, times)))
# #                     minute += str(chose_one)
# #                 else:
# #                     chose_one = max(times)
# #                     minute += str(chose_one)
# #                 times.remove(chose_one)
# #     elif 1 in times:
# #         hour += "1"
# #         times.remove(1)
# #         for i in range(3):
# #             if i == 0:
# #                 chose_one = max(times)
# #                 hour += str(chose_one)
# #             if i == 1:
# #                 chose_one = max(list(filter(lambda x: x <= 6, times)))
# #                 minute += str(chose_one)
# #             if i == 2:
# #                 chose_one = max(times)
# #                 minute += str(chose_one)
# #             times.remove(chose_one)
# #     else:
# #         hour += str(max(times))
# #         for i in range(2):
# #             if i == 0:
# #                 chose_one = max(list(filter(lambda x: x <= 6, times())))
# #                 minute += chose_one
# #             else:
# #                 chose_one = max(times)
# #                 minute += chose_one
# #             times.remove(chose_one)
# #     return str(hour + ":" + minute)


# # # with open("CAU2.INP") as fi:
# # #     times = list(map(int, fi.readline().split()))
# # # times = [1, 2, 3, 4]
# # times = [1, 2, 6, 6]    # bị lỗi
# # # with open("CAU2.OUT", "w") as fo:
# # #     fo.write(calculate(times))
# # print(calculate(times))

from itertools import permutations


def max_hour_from_numbers(a, b, c, d):
    max_hour = -1
    max_minute = -1
    # Tạo ra tất cả các cặp số từ a, b, c, d và tìm giờ lớn nhất
    for hour1, hour2, minute1, minute2 in permutations([a, b, c, d], 4):
        print(hour1, hour2, minute1, minute2)
        print(max_hour, max_minute)
        hour = 10 * hour1 + hour2
        minute = 10 * minute1 + minute2
        if max_hour <= hour < 24 and minute < 60:
            if max_hour == hour:
                if max_minute < minute:
                    max_minute = minute
            else:
                max_hour = hour
                max_minute = minute

    return f"{max_hour:02d}:{max_minute:02d}"


# Thử nghiệm
a, b, c, d = 9, 9, 9, 9
a, b, c, d = 7, 4, 5, 9
a, b, c, d = 1, 2, 3, 4
# a, b, c, d = 7, 4, 5, 0
# a, b, c, d = 7, 4, 0, 0
# a, b, c, d = 7, 0, 0, 0
# a, b, c, d = 9, 0, 0, 0
# a, b, c, d = 0, 0, 0, 0
# a, b, c, d = 9, 8, 0, 0
# a, b, c, d = 2, 4, 0, 0
# a, b, c, d = 2, 9, 5, 3
max_time = max_hour_from_numbers(a, b, c, d)
print("Thời gian có giờ lớn nhất là:", max_time)

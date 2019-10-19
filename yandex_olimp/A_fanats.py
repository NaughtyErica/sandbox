# После футбольного матча фанаты пытаются уехать домой на
# такси. Чтобы сэкономить, они объединяются в группы: фанат
# присоединяется к группе, если знает хотя бы одного человека
# из неё, группа хочет ехать исключительно в одной машине, а
# две разные группы отказываются ехать вместе. Таксопарк владеет
# ограниченным числом машин заданной вместимости. Определите,
# получится ли у таксопарка развезти экономных фанатов.
#
# Формат ввода
# В первой строчке задано число N — число фанатов, во второй
# число М — количество знакомств между фанатами. Далее следует
# M пар чисел от 0 до N-1, разделенных пробелом: каждая пара
# означает обоюдное знакомство между фанатами. Далее следует
# число K — количество типов машин, и K пар вида (вместимость
# машины, количество таких машин). Пары гарантированно уникальны.
#
# 1 <= N <= 1000
#
# 0 <= K <= 1000
#
# Формат вывода
# На выходе должно быть число 1, если у таксопарка получится
# развести фанатов, и 0, если не получится.
#
# Пример 1
# Ввод	    Вывод
# 6           1
# 3
# 0 1
# 1 2
# 4 5
# 2
# 3 2
# 5 1

# Пример 2
# Ввод	    Вывод
# 6           0
# 0
# 1
# 6 5
#
# Пример 3
# Ввод	    Вывод
# 3           0
# 2
# 0 1
# 1 2
# 1
# 2 2

count_fan = int(input())
count_friend_pair = int(input())
friend_pair = []
for i in range(count_friend_pair):
    input_str = input()
    input_set = {int(input_str[0:1]), int(input_str[2:3])}
    friend_pair.append(input_set)

count_type_car = int(input())
content_count_car = []
for n in range(count_type_car):
    input_str = input()
    input_lst = [int(input_str[0:1]), int(input_str[2:3])]
    content_count_car.append(input_lst)

group_friend = []
i = 0
while True:
    if count_friend_pair > 2:
        common_friends = friend_pair[i].intersection(friend_pair[i+1])
        if len(common_friends) > 0:
            friend_pair[i].update(friend_pair[i+1])
            del friend_pair[i+1]
            group_friend.append(friend_pair[i])
            count_pair_remained = len(friend_pair)
            if count_pair_remained > 2:
                continue
            else:
                break
    else:
        break

count_car = 0
for i in range(count_type_car):
    count_car += content_count_car[i][1]

if count_car >= count_fan - len(group_friend):
    print(0)
else:
    print(1)


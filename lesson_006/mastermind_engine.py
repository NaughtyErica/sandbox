import random as rd
search_number_lst = []
user_number_lst = []


def pick_number():
    global search_number_lst
    search_number_lst = []
    list_select = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    step = 0
    while len(search_number_lst) <= 3:
        step += 1
        number = rd.choice(list_select)
        if number != '0' and step == 1:
            list_select.remove(number)
            search_number_lst.append(number)
        elif step > 1:
            list_select.remove(number)
            search_number_lst.append(number)
    # print('Загаданное число', search_number_lst)


def check_number(user_input_str=''):
    global user_number_lst, search_number_lst
    answer = {}
    user_number_lst = list(user_input_str)
    bulls = 0
    cows = 0
    for i in range(len(user_number_lst)):
        if user_number_lst[i] == search_number_lst[i]:
            bulls += 1
            user_number_lst[i] = 'b'
    else:
        for i in range(len(user_number_lst)):
            if user_number_lst[i] in search_number_lst:
                cows += 1
                user_number_lst[i] = 'c'
    answer['bulls'] = bulls
    answer['cows'] = cows
    return answer

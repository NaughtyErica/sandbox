import random as rd
search_number_lst = []
user_number_lst = []


def pick_number():
    global search_number_lst
    search_number_lst = []
    list_select = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    step = 1
    while len(search_number_lst) <= 3:
        number = rd.choice(list_select)
        step += 1
        if number != '0' or step != 1:
            list_select.remove(number)
            search_number_lst.append(number)
#    print('Загаданное число', search_number_lst)


def check_number(user_input_str=''):
    global user_number_lst, search_number_lst
    answer = {}
    user_number_lst = list(user_input_str)
    bulls = 0
    for i in range(len(user_number_lst)):
        if user_number_lst[i] == search_number_lst[i]:
            bulls += 1
    set_search = set(search_number_lst)
    set_user = set(user_number_lst)
    cows = len(set_search & set_user) - bulls
    answer['bulls'] = bulls
    answer['cows'] = cows
    return answer

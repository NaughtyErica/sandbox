# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел


def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n+1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
    return prime_numbers

# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


class PrimeNumbers:

    def __init__(self, n=1):
        self.lower_bound_range = 1
        self.upper_bound_range = n
        self.number = 0
        self.prime = 0
        self.prime_numbers = []

    def __iter__(self):
        return self

    def __next__(self):
        for self.number in range(self.lower_bound_range + 1, self.upper_bound_range + 1):
            for self.prime in self.prime_numbers:
                if self.number % self.prime == 0:
                    break
            else:
                self.prime_numbers.append(self.number)
                self.lower_bound_range = self.number
                return self.number
        raise StopIteration()

#
# prime_number_iterator = PrimeNumbers(n=10000)
# for number in prime_number_iterator:
#     print(number)


# TODO после подтверждения части 1 преподователем, можно делать
# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


def prime_numbers_generator(n):
    prime_numbers = []
    for number in range(2, n+1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
            yield number

#
# for number in prime_numbers_generator(n=10000):
#     print(number)


# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
# Автоморфное число — число, десятичная запись квадрата которого оканчивается цифрами
# самого этого числа. Например, число 625^2 = 390 625, 9 376^2 = 87 909 376,
# 890 625^2 = 793 212 890 625.
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
# ========= полиндромное автоматом сачтливое ==================!!!!
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.

def check_automorphic_number(num=0):
    str_num = str(num)
    len_num = len(str_num)
    square = num * num
    str_square = str(square)
    str_tail_square = str_square[len_num:]
    if str_num == str_tail_square:
        return True
    else:
        return False


def check_for_lucky_number(num=0):
    str_num = str(num)
    len_num = len(str_num)
    sum_left_part = 0
    sum_right_part = 0
    half_len = len_num // 2
    if len_num % 2 == 0:
        middle = half_len
    else:
        middle = half_len + 1
    for i in range(half_len):
        sum_left_part += int(str_num[i])
    for k in range(middle, len_num):
        sum_right_part += int(str_num[k])
    if sum_left_part == sum_right_part and len_num > 1:
        return True
    else:
        return False


def check_palindromic_number(num=0):
    str_num = str(num)
    len_num = len(str_num)

    if len_num % 2 != 0:
        return False
    else:
        half_len = len_num // 2
        left_part_str = str_num[:half_len]
        right_part_str_invert = str_num[:half_len - 1:-1]
        if left_part_str == right_part_str_invert:
            return True
        else:
            return False


def prime_numbers_generator_with_filters(n, *args):
    prime_numbers = []
    function_list = list(args)
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
            quantity_function = len(function_list)
            if quantity_function > 0:
                result_check = False
                for function in function_list:
                    result_check += function(number)
                if result_check == quantity_function:
                    yield number
            else:
                yield number


for number in prime_numbers_generator_with_filters(1000000,
                                                   check_for_lucky_number,
                                                   check_palindromic_number,
                                                   check_automorphic_number,
                                                   ):
    print(number)



# -*- coding: utf-8 -*-

import pprint as pp
# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.


class StatisticCharInFile:

    def __init__(self, file_name):
        self.file_name = file_name
        self.stat_dict = {}
        self.stat_lst = []
        self.char_set = []
        self.total_chars = 0
        self.different_chars = 0
        self.file_content_char = None

    def read_file(self):
        with open(self.file_name, 'r', encoding='cp1251') as file:
            self.file_content_char = file.read()

    def find_frequency_chars(self):
        for char in self.file_content_char:
            if char in self.char_set:
                self.stat_dict[char] += 1
                idx = self.char_set.index(char)
                self.stat_lst[idx] += 1
                self.total_chars += 1
            else:
                if char.isalpha():
                    self.char_set.append(char)
                    self.stat_dict[char] = 1
                    self.stat_lst.append(1)
                    self.different_chars += 1
                    self.total_chars += 1

    @staticmethod
    def item_on_key(dict_for_find, value=None):
        for key, it in dict_for_find.items():
            if it == value:
                return key

    @staticmethod
    def print_line_table(left_width=0, right_width=0, hor_chr='-'):
        print(f'+{hor_chr * left_width}+{hor_chr * right_width}+')

    @staticmethod
    def print_body_line_table(left_str='', right_str='', width=(0, 0), align=(0, 0)):
        """
        variable align can be -1 for left, 0 for center and 1 for right aligned
        in index [0] for left column and index [1] for fight column
       """
        left_str_print = ''
        right_str_print = ''
        if align[0] == 0:
            left_str_print = left_str.center(width[0], ' ')
        elif align[0] == -1:
            left_str_print = left_str + ' ' * (width[0] - len(left_str))
        elif align[0] == 1:
            left_str_print = ' ' * (width[0] - len(left_str)) + left_str

        if align[1] == 0:
            right_str_print = right_str.center(width[1], ' ')
        elif align[1] == -1:
            right_str_print = right_str + ' ' * (width[1] - len(right_str))
        elif align[1] == 1:
            right_str_print = ' ' * (width[1] - len(right_str)) + right_str

        print(f'|{left_str_print}|{right_str_print}|')

    def print_sorted(self, left_width=0, right_width=0):
        self.stat_lst.sort()
        left_str_lst = []
        right_str_lst = []
        for i in range(self.different_chars):
            left_str_lst.append(self.item_on_key(self.stat_dict, self.stat_lst[i]))
            right_str_lst.append(str(self.stat_lst[i]))

        self.print_line_table(left_width=left_width, right_width=right_width, hor_chr='=')
        self.print_body_line_table(left_str='Буква', right_str='Частота',
                                   width=(left_width, right_width), align=(0, 0))
        self.print_line_table(left_width=left_width, right_width=right_width, hor_chr='-')
        for i in range(self.different_chars):
            self.print_body_line_table(left_str=left_str_lst[i], right_str=right_str_lst[i],
                                       width=(left_width, right_width), align=(0, 1))
        self.print_line_table(left_width=left_width, right_width=right_width, hor_chr='-')
        right_str = str(self.different_chars)
        self.print_body_line_table(left_str='Разных', right_str=right_str,
                                   width=(left_width, right_width), align=(0, 1))
        right_str = str(self.total_chars)
        self.print_body_line_table(left_str='Всего', right_str=right_str,
                                   width=(left_width, right_width), align=(0, 1))
        self.print_line_table(left_width=left_width, right_width=right_width, hor_chr='=')

    def print_stat(self):
        self.print_line_table()
        for i in range(self.different_chars):
            print(self.char_set[i], self.stat_lst[i])


find = StatisticCharInFile('python_snippets/voyna-i-mir.txt')
find.read_file()
find.find_frequency_chars()
find.print_sorted(left_width=10, right_width=12)


# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828

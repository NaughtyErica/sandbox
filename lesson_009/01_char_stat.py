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


# class StatisticCharInFile:
#
#     def __init__(self, file_name):
#         self.file_name = file_name
#         self.stat_dict = {}
#         self.stat_lst = []
#         self.char_set = []
#         self.sorted_left_str_lst = []
#         self.sorted_right_str_lst = []
#         self.total_chars = 0
#         self.different_chars = 0
#         self.file_content_char = None
#
#     def read_file(self):
#         with open(self.file_name, 'r', encoding='cp1251') as file:
#             self.file_content_char = file.read()
#
#     def find_frequency_chars(self):
#         for char in self.file_content_char:
#             if char in self.char_set:
#                 self.stat_dict[char] += 1
#                 idx = self.char_set.index(char)
#                 self.stat_lst[idx] += 1
#                 self.total_chars += 1
#             else:
#                 if char.isalpha():
#                     self.char_set.append(char)
#                     self.stat_dict[char] = 1
#                     self.stat_lst.append(1)
#                     self.different_chars += 1
#                     self.total_chars += 1
#
#     @staticmethod
#     def item_on_key(dict_for_find, value=None):
#         for key, it in dict_for_find.items():
#             if it == value:
#                 return key
#
#     @staticmethod
#     def print_line_table(left_width=0, right_width=0, hor_chr='-'):
#         print(f'+{hor_chr * left_width}+{hor_chr * right_width}+')
#
#     @staticmethod
#     def print_body_line_table(left_str='', right_str='', width=(0, 0), align=(0, 0)):
#         """
#         variable align can be -1 for left, 0 for center and 1 for right aligned
#         in align[0] for left column and align[1] for fight column
#        """
#         left_str_print = ''
#         right_str_print = ''
#         if align[0] == 0:
#             left_str_print = left_str.center(width[0], ' ')
#         elif align[0] == -1:
#             left_str_print = left_str + ' ' * (width[0] - len(left_str))
#         elif align[0] == 1:
#             left_str_print = ' ' * (width[0] - len(left_str)) + left_str
#
#         if align[1] == 0:
#             right_str_print = right_str.center(width[1], ' ')
#         elif align[1] == -1:
#             right_str_print = right_str + ' ' * (width[1] - len(right_str))
#         elif align[1] == 1:
#             right_str_print = ' ' * (width[1] - len(right_str)) + right_str
#
#         print(f'|{left_str_print}|{right_str_print}|')
#
#     def sort_stat(self):
#         self.stat_lst.sort(reverse=True)
#         self.sorted_left_str_lst = []
#         self.sorted_right_str_lst = []
#         for i in range(self.different_chars):
#             self.sorted_left_str_lst.append(self.item_on_key(self.stat_dict, self.stat_lst[i]))
#             self.sorted_right_str_lst.append(str(self.stat_lst[i]))
#
#     def print_sorted_stat(self, left_width=0, right_width=0):

#         self.print_line_table(left_width=left_width, right_width=right_width, hor_chr='=')
#         self.print_body_line_table(left_str='Буква', right_str='Частота',
#                                    width=(left_width, right_width), align=(0, 0))
#         self.print_line_table(left_width=left_width, right_width=right_width, hor_chr='-')
#         for i in range(self.different_chars):
#             self.print_body_line_table(left_str=self.sorted_left_str_lst[i], right_str=self.sorted_right_str_lst[i],
#                                        width=(left_width, right_width), align=(0, 1))
#         self.print_line_table(left_width=left_width, right_width=right_width, hor_chr='-')
#         right_str = str(self.different_chars)
#         self.print_body_line_table(left_str='Разных', right_str=right_str,
#                                    width=(left_width, right_width), align=(0, 1))
#         right_str = str(self.total_chars)
#         self.print_body_line_table(left_str='Всего', right_str=right_str,
#                                    width=(left_width, right_width), align=(0, 1))
#         self.print_line_table(left_width=left_width, right_width=right_width, hor_chr='=')
#
#     def print_stat(self):
#         self.print_line_table()
#         for i in range(self.different_chars):
#             print(self.char_set[i], self.stat_lst[i])
#
#
# find = StatisticCharInFile(file_name='python_snippets/voyna-i-mir.txt')
# find.read_file()
# find.find_frequency_chars()
# find.sort_stat()
# find.print_sorted_stat(left_width=10, right_width=12)

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828


from abc import ABCMeta, abstractmethod


class AbstractStatisticClass(metaclass=ABCMeta):
    """
    Абстрактный отряд. Аттрибуты класса, начинающиеся с подчеркивания в python
    являются protected
    """

    def __init__(self, file_name) -> None:
        self.file_name = file_name
        self.stat_dict = {}
        self.stat_lst = []
        self.char_set = []
        self.sorted_left_str_lst = []
        self.sorted_right_str_lst = []
        self.total_chars = 0
        self.different_chars = 0
        self.file_content_char = None

    def make_statistic(self, left_width=0, right_width=0, align=(0, 0)) -> None:
        """
        Шаблонный метод
        """
        self.read_file()
        self.find_frequency_chars()
        self.sort_stat()
        self.print_sorted_stat(left_width=left_width, right_width=right_width, align=align)

    def read_file(self) -> None:
        """
          Чтение текстового файла в кодировке cp1251.
          У всех наследованных классов одинаковый, в шаблон входит
         """
        with open(self.file_name, 'r', encoding='cp1251') as file:
            self.file_content_char = file.read()

    def find_frequency_chars(self) -> None:
        """
         Поиск частот букв в прочитанном файле, заполенение словаря статистикиБ
         Подсчет количества уникальных и суммы букв
         У всех наследованных классов одинаковый, в шаблон входит
        """
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

    @abstractmethod
    def sort_stat(self) -> None:
        """ Определится у каждого конкретного наследованного класса """
        pass

    def print_sorted_stat(self, left_width=0, right_width=0, align=(0, 0)) -> None:
        """

        :param left_width: ширина левой колонки
        :param right_width: ширина правой колонки
        :param align: выравнивание содежжимого колонок в теде таблицы
        Вывод на консоль отсортированной статистики
        У всех наследованных классов одинаковый, в шаблон входит
        """
        self.print_line_table(left_width=left_width, right_width=right_width, hor_chr='=')
        self.print_body_line_table(left_str='Буква', right_str='Частота',
                                   width=(left_width, right_width), align=(0, 0))
        self.print_line_table(left_width=left_width, right_width=right_width, hor_chr='-')
        for i in range(self.different_chars):
            self.print_body_line_table(left_str=self.sorted_left_str_lst[i], right_str=self.sorted_right_str_lst[i],
                                       width=(left_width, right_width), align=align)
        self.print_line_table(left_width=left_width, right_width=right_width, hor_chr='-')
        right_str = str(self.different_chars)
        self.print_body_line_table(left_str='Разных', right_str=right_str,
                                   width=(left_width, right_width), align=(1, 1))
        right_str = str(self.total_chars)
        self.print_body_line_table(left_str='Всего', right_str=right_str,
                                   width=(left_width, right_width), align=(1, 1))
        self.print_line_table(left_width=left_width, right_width=right_width, hor_chr='=')

    @staticmethod
    def print_line_table(left_width=0, right_width=0, hor_chr='-') -> None:
        """
        Вспомогательный метод: печать горизотальной линии границы таблицы
        :param left_width: ширина левой колонки
        :param right_width: ширина правой колонки
        :param hor_chr: символ линии
        В шаблон не входит
        """
        print(f'+{hor_chr * left_width}+{hor_chr * right_width}+')

    @staticmethod
    def print_body_line_table(left_str='', right_str='', width=(0, 0), align=(0, 0)) -> None:
        """
        Вспомогательный метод: печать строки тела таблицы, состоящей из содержимого
        левой колонки и правой с их возможный выравниванием по левому, правому краю или по центру
        :param left_str: содержимое левой колонки
        :param right_str: содержимое правой колонки
        :param width: ширина левой колонки индекс [0] и правой - индекс [1]
        :param align: выравнивание: в левой колонке - индекс [0] и правой - индекс [1]
        значение параметра -1 левое, 0 по центру, 1 правое выравнивание
        В шаблон не входит
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

    def print_stat(self):
        """
        Вспомогательный метод: печать сырой статистики
        В шаблон не входит
        """
        self.print_line_table()
        for i in range(self.different_chars):
            print(self.char_set[i], self.stat_lst[i])


class StatSortFrequency(AbstractStatisticClass):

    def __init__(self, file_name, desc=True):
        super().__init__(file_name=file_name)
        self.desc = desc

    @staticmethod
    def item_on_key(dict_for_find, value=None):
        """
        Вспомогательный метод получения из словаря ключа по его заначению
        :param dict_for_find: словарь для поиска
        :param value: значение, по которому ищется его ключ
        :return: ключ
        """
        for key, it in dict_for_find.items():
            if it == value:
                return key

    def sort_stat(self):
        """
        Конкретная реализация абстарктного метода из унаследованного класса:
        сортировка результатаов статистики по убыванию частоты символа
        :param desc: принимает True - убывание, False - возрастание
        """
        self.stat_lst.sort(reverse=self.desc)
        self.sorted_left_str_lst = []
        self.sorted_right_str_lst = []
        for i in range(self.different_chars):
            self.sorted_left_str_lst.append(self.item_on_key(self.stat_dict, self.stat_lst[i]))
            self.sorted_right_str_lst.append(str(self.stat_lst[i]))


stat_sort1 = StatSortFrequency(file_name='python_snippets/voyna-i-mir.txt', desc=True)
stat_sort1.make_statistic(left_width=10, right_width=10, align=(0, 1))

stat_sort2 = StatSortFrequency(file_name='python_snippets/voyna-i-mir.txt', desc=False)
stat_sort2.make_statistic(left_width=10, right_width=10, align=(0, 1))



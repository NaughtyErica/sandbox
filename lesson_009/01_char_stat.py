# -*- coding: utf-8 -*-

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
#     def item_on_key(dict_for_find={}, value=None):
#         for key, it in dict_for_find.items():
#             if it == value:
#                 dict_for_find[key] = 0
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
import lesson_009.speed_metr as sm


class AbstractStatisticClass(metaclass=ABCMeta):
    """
    Абстрактный класс сбора и вывода статистики по буквам в текстовом файле
    """

    def __init__(self, file_name='') -> None:
        """
        :param file_name: имя входного файла для сбора статистики
        """
        self.file_name = file_name
        self.stat_dict = {}
        self.sorted_left_str_lst = []
        self.sorted_right_str_lst = []
        self.total_chars = 0
        self.different_chars = 0
        self.file_content_char = None

    def make_statistic(self, left_width=0, right_width=0, align=(0, 0)) -> None:
        """
        Шаблонный метод
        """
        self.read_file_line()
        self.sort_stat()
        self.print_sorted_stat(left_width=left_width, right_width=right_width, align=align)

    def _read_file_all(self) -> None:
        """
        Внутренний вспомогательный метод:
        чтение текстового файла целиком в переменную self.file_content_char в кодировке cp1251.
        Для отладки
        """
        with open(self.file_name, 'r', encoding='cp1251') as file:
            self.file_content_char = file.read()

    def read_file_line(self) -> None:
        """
        Метод входит в шаблон:
        чтение текстового файла по строкам в переменную line в кодировке cp1251.
        У всех наследованных классов одинаковый, в шаблон включаем, как основной метод
        в цикле чтения вызывает метод заполение сатитстики _find_frequency_chars
        """
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                self._find_frequency_chars(line=line)

    def _find_frequency_chars(self, line='') -> None:
        """
        Внутренний вспомогательный метод:
        Поиск частот букв в прочитанном файле, заполенение словаря статистики
        Подсчет количества уникальных и суммы букв
        """
        for char in line:
            if char in self.stat_dict.keys():
                self.stat_dict[char] += 1
                self.total_chars += 1
            else:
                if char.isalpha():
                    self.stat_dict[char] = 1
                    self.different_chars += 1
                    self.total_chars += 1

    @abstractmethod
    def sort_stat(self) -> None:
        """
        Абстрактый метод
        Входит в шаблон
        Определится у каждого конкретного наследованного класса
        """
        pass

    def print_sorted_stat(self, left_width=0, right_width=0, align=(0, 0)) -> None:
        """
        Метод вывода на консоль отсортированной статистики
        Входит в шаблон
        :param left_width: ширина левой колонки
        :param right_width: ширина правой колонки
        :param align: выравнивание содежжимого колонок в теде таблицы
        """
        self._print_line_table(left_width=left_width, right_width=right_width, hor_chr='=')
        self._print_body_line_table(left_str='Буква', right_str='Частота',
                                    width=(left_width, right_width), align=(0, 0))
        self._print_line_table(left_width=left_width, right_width=right_width, hor_chr='-')
        for i in range(self.different_chars):
            self._print_body_line_table(left_str=self.sorted_left_str_lst[i], right_str=self.sorted_right_str_lst[i],
                                        width=(left_width, right_width), align=align)
        self._print_line_table(left_width=left_width, right_width=right_width, hor_chr='-')
        right_str = str(self.different_chars)
        self._print_body_line_table(left_str='Разных', right_str=right_str,
                                    width=(left_width, right_width), align=(1, 1))
        right_str = str(self.total_chars)
        self._print_body_line_table(left_str='Всего', right_str=right_str,
                                    width=(left_width, right_width), align=(1, 1))
        self._print_line_table(left_width=left_width, right_width=right_width, hor_chr='=')

    @staticmethod
    def _print_line_table(left_width=0, right_width=0, hor_chr='-') -> None:
        """
        Вспомогательный статический метод: печать горизотальной линии границы таблицы
        :param left_width: ширина левой колонки
        :param right_width: ширина правой колонки
        :param hor_chr: символ линии
        """
        print(f'+{hor_chr * left_width}+{hor_chr * right_width}+')

    @staticmethod
    def _print_body_line_table(left_str='', right_str='', width=(0, 0), align=(0, 0)) -> None:
        """
        Вспомогательный статический метод: печать строки тела таблицы, состоящей из содержимого
        левой колонки и правой с их возможный выравниванием по левому, правому краю или по центру
        :param left_str: содержимое левой колонки
        :param right_str: содержимое правой колонки
        :param width: ширина левой колонки индекс [0] и правой - индекс [1]
        :param align: выравнивание: в левой колонке - индекс [0] и правой - индекс [1]
        значение параметра -1 левое, 0 по центру, 1 правое выравнивание
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

    def _print_stat(self) -> None:
        """
        Вспомогательный метод: печать сырой статистики
        для отладки
        """
        for char in self.stat_dict.keys():
            print(char, self.stat_dict[char])
        print(self.different_chars, self.total_chars)


class StatSortFrequency(AbstractStatisticClass):
    """
    Класс потомок с реальзацие сортировки по частоте символов
    """
    def __init__(self, file_name='', desc=True):
        super().__init__(file_name=file_name)
        self.desc = desc
        self.stat_lst = []

    def sort_stat(self):
        """
        Конкретная реализация абстарктного метода из унаследованного класса:
        сортировка результатаов статистики по убыванию частоты символа
        :param desc: принимает True - убывание, False - возрастание
        """
        self.stat_lst = sorted(self.stat_dict.items(), key=lambda item: item[1], reverse=self.desc)
        for i in range(self.different_chars):
            self.sorted_left_str_lst.append(self.stat_lst[i][0])
            self.sorted_right_str_lst.append(str(self.stat_lst[i][1]))


class StatSortAlpha(AbstractStatisticClass):
    """
    Класс потомок с реализацией сортировки по алфавиту
    """
    def __init__(self, file_name, desc=True):
        super().__init__(file_name=file_name)
        self.desc = desc
        self.char_lst = []

    def sort_stat(self):
        """
        Конкретная реализация абстарктного метода из унаследованного класса:
        сортировка результатаов статистики по убыванию или возрастанию символа
        :param desc: принимает True - убывание, False - возрастание
        """
        for char in self.stat_dict.keys():
            self.char_lst.append(char)
        self.char_lst.sort(reverse=self.desc)
        for char in self.char_lst:
            self.sorted_left_str_lst.append(char)
            self.sorted_right_str_lst.append(str(self.stat_dict[char]))


time_stat = sm.SpeedMetrics()
time_stat.start(name_process='Время выполения задачи')
# stat_sort1 = StatSortFrequency(file_name='python_snippets/voyna-i-mir.txt', desc=True)
# stat_sort1.make_statistic(left_width=10, right_width=10, align=(0, 1))
#
stat_sort2 = StatSortFrequency(file_name='python_snippets/voyna-i-mir.txt', desc=True)
stat_sort2.make_statistic(left_width=8, right_width=10, align=(1, 1))
#
# stat_sort3 = StatSortAlpha(file_name='python_snippets/voyna-i-mir.txt', desc=False)
# stat_sort3.make_statistic(left_width=10, right_width=10, align=(0, 1))

# stat_sort4 = StatSortAlpha(file_name='python_snippets/voyna-i-mir.txt', desc=True)
# stat_sort4.make_statistic(left_width=10, right_width=10, align=(0, 1))

time_stat.get_interval()

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


# class CharFrequenciesInFile:
#
#     def __init__(self, file_name):
#         self.file_name = file_name
#         self.dict_char_frequencies = {}
#         self.lst_frequencies = []
#         self.lst_sorted_cells_left_column_table = []
#         self.lst_sorted_cells_right_column_table = []
#         self.total_chars = 0
#         self.different_chars = 0
#         self.file_contents = None
#
#     def read_file(self):
#         """
#         Чтение текстового файла целиком в переменную self.file_contents в кодировке cp1251.
#         """
#         with open(self.file_name, 'r', encoding='cp1251') as file:
#             self.file_contents = file.read()
#
#     def find_frequency_chars(self):
#         """
#         Поиск частот букв в прочитанном файле, заполенение словаря частот символов
#         Подсчет количества уникальных букв и суммарное количество букв в файле
#         """
#         for char in self.file_contents:
#             if char in self.dict_char_frequencies.keys():
#                 self.dict_char_frequencies[char] += 1
#                 self.total_chars += 1
#             else:
#                 if char.isalpha():
#                     self.dict_char_frequencies[char] = 1
#                     self.different_chars += 1
#                     self.total_chars += 1
#
#     @staticmethod
#     def item_on_key(dict_for_find={}, value=None):
#         """
#         Вспомогательный статический метод поиска ключа по значению
#         для исключения выбора одного и того же ключа при одинаковых значениях,
#         переданное значение после нахождения ключа обнуляется,
#         исключая таким образом повторное его использование
#         :param dict_for_find: словарь для поиска
#         :param value: значение ключа
#         :return: найденный ключ
#         """
#         for key, it in dict_for_find.items():
#             if it == value:
#                 dict_for_find[key] = 0
#                 return key
#
#     @staticmethod
#     def print_hor_line_table_border(left_width=0, right_width=0, hor_chr='-'):
#         """
#         Статический метод: печать горизотальной линии границы таблицы
#         :param left_width: ширина левой колонки
#         :param right_width: ширина правой колонки
#         :param hor_chr: символ линии
#         """
#         print(f'+{hor_chr * left_width}+{hor_chr * right_width}+')
#
#     @staticmethod
#     def print_table_row(left_str='', right_str='', width=(0, 0), align=(0, 0)):
#         """
#         Статический метод: печать строки тела таблицы, состоящей из содержимого
#         левой колонки и правой с их возможный выравниванием по левому, правому краю или по центру
#         :param left_str: содержимое левой колонки
#         :param right_str: содержимое правой колонки
#         :param width: ширина левой колонки индекс [0] и правой - индекс [1]
#         :param align: выравнивание: в левой колонке - индекс [0] и правой - индекс [1]
#         значение параметра - 1 левое, 0 по центру, 1 правое выравнивание
#         """
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
#     def _sort_stat(self):
#         """
#         Внутренний метод
#         Сортировка результатаов статистики по убыванию частоты символа
#         """
#         for char in self.dict_char_frequencies.keys():
#             self.lst_frequencies.append(self.dict_char_frequencies[char])
#         self.lst_frequencies.sort(reverse=True)
#         for i in range(self.different_chars):
#             self.lst_sorted_cells_left_column_table.append(self.item_on_key(self.dict_char_frequencies,
#                                                                             self.lst_frequencies[i]))
#             self.lst_sorted_cells_right_column_table.append(str(self.lst_frequencies[i]))
#
#     def print_sorted_stat(self, left_width=0, right_width=0):
#         """
#         Метод вывода на консоль отсортированной по убыванию частоты символов статистики
#         :param left_width: ширина левой колонки
#         :param right_width: ширина правой колонки
#         """
#         self._sort_stat()
#         self.print_hor_line_table_border(left_width=left_width, right_width=right_width, hor_chr='=')
#         self.print_table_row(left_str='Буква', right_str='Частота',
#                              width=(left_width, right_width), align=(0, 0))
#         self.print_hor_line_table_border(left_width=left_width, right_width=right_width, hor_chr='-')
#         for i in range(self.different_chars):
#             self.print_table_row(left_str=self.lst_sorted_cells_left_column_table[i],
#                                  right_str=self.lst_sorted_cells_right_column_table[i],
#                                  width=(left_width, right_width), align=(0, 1))
#         self.print_hor_line_table_border(left_width=left_width, right_width=right_width, hor_chr='-')
#         right_str = str(self.different_chars)
#         self.print_table_row(left_str='Разных', right_str=right_str,
#                              width=(left_width, right_width), align=(0, 1))
#         right_str = str(self.total_chars)
#         self.print_table_row(left_str='Всего', right_str=right_str,
#                              width=(left_width, right_width), align=(0, 1))
#         self.print_hor_line_table_border(left_width=left_width, right_width=right_width, hor_chr='=')
#
#     def print_stat(self):
#         """
#         Вспомогательный метод
#         печать сырой статистики для отладки
#         """
#         for char in self.dict_char_frequencies.keys():
#             print(char, self.dict_char_frequencies[char])
#
#
# find = CharFrequenciesInFile(file_name='python_snippets/voyna-i-mir.txt')
# find.read_file()
# find.find_frequency_chars()
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
        self.dict_char_frequencies = {}
        self.lst_sorted_cells_left_column_table = []
        self.lst_sorted_cells_right_column_table = []
        self.total_chars = 0
        self.different_chars = 0
        self.file_contents = None

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
        чтение текстового файла целиком в переменную self.file_contents в кодировке cp1251.
        Для отладки
        """
        with open(self.file_name, 'r', encoding='cp1251') as file:
            self.file_contents = file.read()

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
        Поиск частот букв в прочитанном файле, заполенение словаря частот символов
        Подсчет количества уникальных букв и суммарное количество букв в файле
        :param line: строка, передаваемая из читаемого файла
        """
        for char in line:
            if char in self.dict_char_frequencies.keys():
                self.dict_char_frequencies[char] += 1
                self.total_chars += 1
            else:
                if char.isalpha():
                    self.dict_char_frequencies[char] = 1
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
        :param align: выравнивание содежжимого колонок в теле таблицы
        """
        self._print_hor_line_table_border(left_width=left_width, right_width=right_width, hor_chr='=')
        self._print_table_row(left_str='Буква', right_str='Частота',
                              width=(left_width, right_width), align=(0, 0))
        self._print_hor_line_table_border(left_width=left_width, right_width=right_width, hor_chr='-')
        for i in range(self.different_chars):
            self._print_table_row(left_str=self.lst_sorted_cells_left_column_table[i],
                                  right_str=self.lst_sorted_cells_right_column_table[i],
                                  width=(left_width, right_width), align=align)
        self._print_hor_line_table_border(left_width=left_width, right_width=right_width, hor_chr='-')
        right_str = str(self.different_chars)
        self._print_table_row(left_str='Разных', right_str=right_str,
                              width=(left_width, right_width), align=(1, 1))
        right_str = str(self.total_chars)
        self._print_table_row(left_str='Всего', right_str=right_str,
                              width=(left_width, right_width), align=(1, 1))
        self._print_hor_line_table_border(left_width=left_width, right_width=right_width, hor_chr='=')

    @staticmethod
    def _print_hor_line_table_border(left_width=0, right_width=0, hor_chr='-') -> None:
        """
        Вспомогательный статический метод: печать горизотальной линии границы таблицы
        :param left_width: ширина левой колонки
        :param right_width: ширина правой колонки
        :param hor_chr: символ линии
        """
        print(f'+{hor_chr * left_width}+{hor_chr * right_width}+')

    @staticmethod
    def _print_table_row(left_str='', right_str='', width=(0, 0), align=(0, 0)) -> None:
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
        for char in self.dict_char_frequencies.keys():
            print(char, self.dict_char_frequencies[char])
        print(self.different_chars, self.total_chars)


class StatSortFrequency(AbstractStatisticClass):
    """
    Класс потомок с реальзацие сортировки по частоте символов
    """
    def __init__(self, file_name='', desc=True):
        """
        :param file_name: Имя файла, передается в родительсикй класс
        :param desc: True - убывание, False - возрастание
        """
        super().__init__(file_name=file_name)
        self.desc = desc
        self.lst_frequencies = []

    def sort_stat(self):
        """
        Конкретная реализация абстарктного метода из унаследованного класса:
        сортировка результатаов статистики по убыванию или возрастанию частоты символа
        """
        self.lst_frequencies = sorted(self.dict_char_frequencies.items(),
                                      key=lambda item: item[1], reverse=self.desc)
        for i in range(self.different_chars):
            self.lst_sorted_cells_left_column_table.append(self.lst_frequencies[i][0])
            self.lst_sorted_cells_right_column_table.append(str(self.lst_frequencies[i][1]))


class StatSortAlpha(AbstractStatisticClass):
    """
    Класс потомок с реализацией сортировки по алфавиту
    """
    def __init__(self, file_name, desc=True):
        """
        :param file_name: Имя файла, передается в родительсикй класс
        :param desc:  False - алфавитный порядок, True - обратный алфавитному
        """
        super().__init__(file_name=file_name)
        self.desc = desc
        self.lst_chars = []

    def sort_stat(self):
        """
        Конкретная реализация абстарктного метода из унаследованного класса:
        сортировка результатов статистики по убыванию или возрастанию символа
        """
        for char in self.dict_char_frequencies.keys():
            self.lst_chars.append(char)
        self.lst_chars.sort(reverse=self.desc)
        for char in self.lst_chars:
            self.lst_sorted_cells_left_column_table.append(char)
            self.lst_sorted_cells_right_column_table.append(str(self.dict_char_frequencies[char]))


time_stat = sm.SpeedMetrics()
time_stat.start(name_process='Время выполения задачи')
# stat_sort1 = StatSortFrequency(file_name='python_snippets/voyna-i-mir.txt', desc=True)
# stat_sort1.make_statistic(left_width=10, right_width=10, align=(0, 1))
#
# stat_sort2 = StatSortFrequency(file_name='python_snippets/voyna-i-mir.txt', desc=True)
# stat_sort2.make_statistic(left_width=8, right_width=10, align=(1, 1))
#
stat_sort3 = StatSortAlpha(file_name='python_snippets/voyna-i-mir.txt', desc=False)
stat_sort3.make_statistic(left_width=10, right_width=10, align=(0, 1))

# stat_sort4 = StatSortAlpha(file_name='python_snippets/voyna-i-mir.txt', desc=True)
# stat_sort4.make_statistic(left_width=10, right_width=10, align=(0, 1))

time_stat.get_interval()

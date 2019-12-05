# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# который читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234
# ================= импорт модуля из lesson_009 не проходит из за имени файла, начинающегося на
# цифру ============ 02_log_parser.py ========= пришлось копировать все содержимое классов сюда

from abc import ABCMeta, abstractmethod
from datetime import datetime
import re
import sys
import os

LOG_ENTRY_RE = '\[\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\.\d{6}\]\sN?OK'


class AbstractParserClass(metaclass=ABCMeta):
    """
    Абстрактный класс парсинга лога и записи отчета в текстовый файл
    Используется паттерн: Шаблонный метод
    """
    def __init__(self, input_file_name='', output_file_name='') -> None:
        """
        :param input_file_name: имя входного файла лога
        :param output_file_name: имя выходного файла с отчетом по логу
        """
        self.input_file_name = input_file_name
        self.output_file_name = output_file_name
        self.log_list = []
        self.str_out_list = []
        self.path_root = os.path.dirname(__file__)

    def read_input_file(self) -> None:
        """
        Метод входит в шаблон:
        чтение файла лога в список
        Ссылка не регулярку https://regex101.com/r/a6L1VC/1
        """
        path_input_file = os.path.join(self.path_root, self.input_file_name)
        if os.path.isfile(path_input_file):
            input_file = open(self.input_file_name, mode='r', encoding='utf8')
        else:
            sys.exit(f'Файл {self.input_file_name} не найден в текущем каталоге!')
        for line in input_file:
            if re.match(LOG_ENTRY_RE, line) is None:
                input_file.close()
                print(line)
                sys.exit('Не соотвествие строки файла шаблону')
            else:
                self.log_list.append(line)
        input_file.close()

    def write_output_file(self) -> None:
        """
        Метод входит в шаблон:
        запись файла отчета
        """
        output_file = open(self.output_file_name, mode='w', encoding='utf8')
        output_file.writelines(self.str_out_list)
        output_file.close()

    def parse(self) -> None:
        """
        Шаблонный метод
        """
        self.read_input_file()
        self.parse_lines()
        self.write_output_file()

    @abstractmethod
    def parse_lines(self) -> None:
        """
        Абстрактый метод
        Входит в шаблон
        Определится у каждого конкретного наследованного класса
        """
        pass


class ParserLog(AbstractParserClass):
    """
    Класс потомок с реализацией парсинга
    """
    def __init__(self, input_file_name='', output_file_name='', select='NOK', interval='M'):
        """
        :param input_file_name: имя входного файла лога
        :param output_file_name: имя выходного файла с отчетом по логу
        передаем в родительский класс через вызов конструктора
        :param select: искомое выражение, в нашем случае OK или NOK
        :param interval: интервал группировки, принмает значания
        Y - год, m - месяц, d - день, H - час, M - минута
        """
        super().__init__(input_file_name=input_file_name, output_file_name=output_file_name, )
        self.select = select
        self.interval = interval
        self.count_select = 0
        self.prev_date = None
        self.date = None
        self.assigned_values = False

    def _assign_values(self):
        """
        Вспомогательный метод для выполения одинаковых действий
        внутри парсинга при разных периодах группировки
        """
        str_date = self.prev_date.strftime("%Y-%m-%d %H:%M")
        str_out = f'[{str_date}]  {self.count_select} \n'
        self.str_out_list.append(str_out)
        self.count_select = 0
        self.assigned_values = True

    def parse_lines(self):
        """
        Конкретная реализация абстарктного метода из унаследованного класса:
        посчет количества искомых значений select для различных периодов
        """
        for line in self.log_list:
            if self.select in line:
                self.date = datetime.strptime(line[1:20], "%Y-%m-%d %H:%M:%S")
                if self.prev_date:
                    self.count_select += 1
                    if self.interval == 'M':
                        if self.date.minute > self.prev_date.minute:
                            self._assign_values()
                    elif self.interval == 'H':
                        if self.date.hour > self.prev_date.hour:
                            self._assign_values()
                    elif self.interval == 'd':
                        if self.date.day > self.prev_date.day:
                            self._assign_values()
                    elif self.interval == 'm':
                        if self.date.month > self.prev_date.month:
                            self._assign_values()
                    elif self.interval == 'Y':
                        if self.date.year > self.prev_date.year:
                            self._assign_values()
                self.prev_date = self.date
        if not self.assigned_values:
            self.prev_date = self.date
            self._assign_values()


# ================Создаю потомка на основе имеющегося класса, не изменив в нем ни строчки кода===============
class ParserLogIterator(ParserLog):

    def __init__(self, input_file_name='', output_file_name='prn', select='NOK', interval='M'):
        """
        Инициализируем все поля, передаем в родительский метод запрет
        создания выходгного файла, проводим парсинг, список готов к выдаче значений итератором
        """
        super().__init__(input_file_name=input_file_name,
                         output_file_name=output_file_name,
                         select=select, interval=interval)
        self.parse()
        self.position_in_out_list = -1
        self.count_line_in_out_list = len(self.str_out_list)

    def __iter__(self):
        """
        Добавляем метод __iter__
        """
        return self

    def __next__(self):
        """
        Реализуем выдачу следующего значения
        """
        self.position_in_out_list += 1
        if self.position_in_out_list < self.count_line_in_out_list:
            return_str = self.str_out_list[self.position_in_out_list].rsplit(' ')
            return f'{return_str[0]} {return_str[1]}', return_str[3]
        else:
            raise StopIteration()

    def write_output_file(self):
        """
        Переопределяем запись результата в файл для итератора,
        пусть он просто ничего не делает!
        """
        if self.output_file_name == 'prn':
            pass


par = ParserLogIterator(input_file_name='events.txt', select='OK', interval='H')

for group_time, event_count in par:
    print(f'{group_time} {event_count}')



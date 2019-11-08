# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

from abc import ABCMeta, abstractmethod
from datetime import datetime


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

    def read_input_file(self) -> None:
        """
        Метод входит в шаблон:
        чтение файла лога в список
        """
        input_file = open(self.input_file_name, mode='r', encoding='utf8')
        for line in input_file:
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

    def parser(self) -> None:
        """
        Шаблонный метод
        """
        self.read_input_file()
        self.parser_lines()
        self.write_output_file()

    @abstractmethod
    def parser_lines(self) -> None:
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
    def __init__(self, input_file_name='', output_file_name='', select='NOK', interval='s'):
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

    def parser_lines(self):
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


par = ParserLog(input_file_name='events.txt', output_file_name='out.txt',
                select='NOK', interval='M')
par.parser()

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828

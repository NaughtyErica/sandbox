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
import lesson_009.speed_metr as sm


class AbstractParserClass(metaclass=ABCMeta):

    def __init__(self, input_file_name='', output_file_name='') -> None:
        self.input_file_name = input_file_name
        self.output_file_name = output_file_name
        self.stat_dict = {}
        self.statistic_line = ''
        self.log_list = []

    def read_write_files(self) -> None:
        input_file = open(self.input_file_name, mode='r', encoding='utf8')
        output_file = open(self.output_file_name, mode='w', encoding='utf8')
        line = True
        while line:
            line = input_file.readline()
            if 'NOK' in line:
                i = 0
                date_time = None

        input_file.close()
        output_file.close()

    @abstractmethod
    def parser_line(self, line='') -> None:
        pass


class ParserLog(AbstractParserClass):

    def parser_line(self, line=''):
        prev_date = None
        count_nok = 0
        with open(self.input_file_name) as input_file:
            for line in input_file:
                if 'NOK'in line:
                    date = datetime.strptime(line[1:20], "%Y-%m-%d %H:%M:%S")
                    if prev_date:
                        count_nok += 1
                        if date.minute > prev_date.minute:
                            str_date = prev_date.strftime("%Y-%m-%d-%H.%M")
                            str_out = f'[{str_date}]  {count_nok}'
                            print(str_out)
                            count_nok = 0
                    prev_date = date


par = ParserLog(input_file_name='events.txt')
par.parser_line()

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828

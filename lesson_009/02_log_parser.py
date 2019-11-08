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
        self.log_list = []
        self.str_out_list = []

    def read_input_file(self) -> None:
        input_file = open(self.input_file_name, mode='r', encoding='utf8')
        for line in input_file:
            self.log_list.append(line)
        input_file.close()

    def write_output_file(self) -> None:
        output_file = open(self.output_file_name, mode='w', encoding='utf8')
        output_file.writelines(self.str_out_list)
        output_file.close()

    def parser(self):
        self.read_input_file()
        self.parser_lines()
        self.write_output_file()

    @abstractmethod
    def parser_lines(self) -> None:
        pass


class ParserLog(AbstractParserClass):

    def __init__(self, input_file_name='', output_file_name='', select='NOK', interval='s'):
        super().__init__(input_file_name=input_file_name, output_file_name=output_file_name, )
        self.select = select
        # select принмает значания Y - год, m - месяц, d - день, H - час, M - минута
        self.interval = interval

    # def parser_lines(self):
    #     prev_date = None
    #     count_nok = 0
    #     input_file = open(self.input_file_name, mode='r', encoding='utf8')
    #     for line in input_file:
    #         if 'NOK'in line:
    #             date = datetime.strptime(line[1:20], "%Y-%m-%d %H:%M:%S")
    #             if prev_date:
    #                 count_nok += 1
    #                 if date.minute > prev_date.minute:
    #                     str_date = prev_date.strftime("%Y-%m-%d %H.%M")
    #                     str_out = f'[{str_date}]  {count_nok}'
    #                     print(str_out)
    #                     count_nok = 0
    #             prev_date = date
    #     input_file.close()

    def parser_lines(self):
        prev_date = None
        count_select = 0

        for line in self.log_list:
            if self.select in line:
                date = datetime.strptime(line[1:20], "%Y-%m-%d %H:%M:%S")
                if prev_date:
                    count_select += 1
                    if self.interval == 'M':
                        if date.minute > prev_date.minute:
                            str_date = prev_date.strftime("%Y-%m-%d %H.%M")
                            str_out = f'[{str_date}]  {count_select} \n'
                            self.str_out_list.append(str_out)
                            count_select = 0
                    elif self.interval == 'H':
                        if date.hour > prev_date.hour:
                            str_date = prev_date.strftime("%Y-%m-%d %H.%M")
                            str_out = f'[{str_date}]  {count_select} \n'
                            self.str_out_list.append(str_out)
                            count_select = 0
                    elif self.interval == 'd':
                        if date.day > prev_date.day:
                            str_date = prev_date.strftime("%Y-%m-%d %H.%M")
                            str_out = f'[{str_date}]  {count_select} \n'
                            self.str_out_list.append(str_out)
                            count_select = 0

                prev_date = date


par = ParserLog(input_file_name='events.txt', output_file_name='out.txt', select='NOK', interval='d')
par.parser()

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828

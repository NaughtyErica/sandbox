# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПРОЦЕССНОМ стиле
#
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
from lesson_012.python_snippets.utils import time_track
import multiprocessing
import re
import sys
import os


TICKER_ENTRY_RE = '\w{3}\d{1},\d{2}:\d{2}:\d{2},\d{1,}.\d{4},\d{1,}'
TITLE_STR = 'SECID,TRADETIME,PRICE,QUANTITY\n'


class VolatilityTicker(multiprocessing.Process):
    """
    Класс рассчета волатильности тикера из одного файла
    с применением процессов, используя очередь, переданную из вызывающего процесса,
    для передачи вычиленных значений в родительский процесс
    """

    def __init__(self, input_file_name, collector, *args, **kwargs):
        """
        :param input_file_name имя входного файла
        :param collector ссылка на очередь для передачи
        вычисленных значений в родительский процесс
        *args, **kwargs уходят к родителю
        """
        super().__init__(*args, **kwargs)
        self.tickers_list_collector = collector
        self.input_file_name = input_file_name
        self.path_root = os.path.dirname(__file__)
        self.ticker_price_list = []
        self.count_line_in_ticker_file = 0
        self.ticker_name = ''
        self.sum_price = 0
        self.avg_price = 0
        self.volatility = 0

    def read_input_file(self):
        """
        Чтение файла тикера в список self.ticker_price_list
        регулярка https://regex101.com/r/FKEeIw/1
        """
        path_input_file = os.path.join(self.path_root, self.input_file_name)
        if os.path.isfile(path_input_file):
            input_file = open(self.input_file_name, mode='r', encoding='utf8')
        else:
            sys.exit(f'Файл {self.input_file_name} не найден в текущем каталоге!')
        title_str = input_file.readline()
        if title_str != TITLE_STR:
            input_file.close()
            print(title_str)
            sys.exit('Неверный заголовок CSV-файла')
        sec_id = None
        for line in input_file:
            if re.match(TICKER_ENTRY_RE, line) is None:
                input_file.close()
                print(line)
                sys.exit('Не соотвествие строки файла шаблону')
            else:
                sec_id, trade_time, price, quantity = line.split(',')
                self.ticker_price_list.append(float(price))
        self.ticker_name = sec_id
        self.count_line_in_ticker_file = len(self.ticker_price_list)
        input_file.close()

    def calculate_volatility(self):
        """
        Метод рассчета волатильности тикера сумме всех записей в файле
        """
        for price in self.ticker_price_list:
            self.sum_price += price
        self.avg_price = self.sum_price / self.count_line_in_ticker_file
        self.ticker_price_list.sort()
        self.volatility = (self.ticker_price_list[self.count_line_in_ticker_file - 1] -
                           self.ticker_price_list[0]) / self.avg_price * 100

    def run(self):
        """
        Чтение файла тикера и рассчет по нему
        волатильности для этого тикера и
        передача списка в очередь
        """
        self.read_input_file()
        self.calculate_volatility()
        for_put = [self.volatility, self.ticker_name]
        self.tickers_list_collector.put(for_put)


class VolatilityTickersOnDir:
    """
    Класс рассчета волатильности по группе файлов, находящихся в исходной папке
    и выводов результатов на консоль с использованием процессов
    """
    def __init__(self, source_dir='', ):
        """
        :param source_dir: имя исходной папки с файлами
        """
        self.path_root = os.path.dirname(__file__)
        self.path_source = os.path.join(self.path_root, source_dir)
        self.tickers_volatility_list = []
        self.zero_tickers_volatility_list = []
        self.count_tickers_non_zero = 0
        self.input_file_name_list = []

    def execute(self):
        """
        Проход в цикле по всем файлам исходной папки
        с заполенением списка исходных файлов self.input_file_name_list
        Создание серии объектов по классу VolatilityTicker для
        рассчета волатильности по каждому файлу и
        запуск этих объектов в мульти-процессы
        Получение из очереди вычисленных там значений и заполение ими списков
        self.tickers_volatility_list
        self.zero_tickers_volatility_list
        """
        for dir_path, dir_names, file_names in os.walk(self.path_source):
            for file_name in file_names:
                path_input_file = os.path.join(self.path_source, file_name)
                self.input_file_name_list.append(path_input_file)

        collector_for_ticker_list = multiprocessing.Queue()
        tickers = [VolatilityTicker(input_file_name=name, collector=collector_for_ticker_list)
                   for name in self.input_file_name_list]

        for ticker in tickers:
            ticker.start()
        for ticker in tickers:
            ticker.join()
        while not collector_for_ticker_list.empty():
            list_from_collector = collector_for_ticker_list.get()
            if list_from_collector[0] == 0.0:
                self.zero_tickers_volatility_list.append(list_from_collector[1])
            else:
                self.tickers_volatility_list.append(list_from_collector)

    def print_result(self):
        """
        Печать полученных результатов на консоль согласно задания
        """
        self.tickers_volatility_list.sort()
        self.zero_tickers_volatility_list.sort()
        print('Максимальная волатильность:')
        for i in [2, 1, 0]:
            print(self.tickers_volatility_list[i][1], '--', '%.2f' % (self.tickers_volatility_list[i][0]))
        max_element = len(self.tickers_volatility_list)
        print('Минимальная волатильность:')
        for i in [max_element - 1, max_element - 2, max_element - 3]:
            print(self.tickers_volatility_list[i][1], '--', '%.2f' % (self.tickers_volatility_list[i][0]))
        print('Нулевая волатильность:')
        for ticker in self.zero_tickers_volatility_list:
            print(ticker, end=' ')
        print()


@time_track
def main():
    tickers = VolatilityTickersOnDir(source_dir='trades')
    tickers.execute()
    tickers.print_result()


if __name__ == '__main__':
    main()

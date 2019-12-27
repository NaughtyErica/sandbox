# -*- coding: utf-8 -*-


# Описание предметной области:
#
# При торгах на бирже совершаются сделки - один купил, второй продал.
# Покупают и продают ценные бумаги (акции, облигации, фьючерсы, етс). Ценные бумаги - это по сути долговые расписки.
# Ценные бумаги выпускаются партиями, от десятка до несколько миллионов штук.
# Каждая такая партия (выпуск) имеет свой торговый код на бирже - тикер - https://goo.gl/MJQ5Lq
# Все бумаги из этой партии (выпуска) одинаковы в цене, поэтому говорят о цене одной бумаги.
# У разных выпусков бумаг - разные цены, которые могут отличаться в сотни и тысячи раз.
# Каждая биржевая сделка характеризуется:
#   тикер ценнной бумаги
#   время сделки
#   цена сделки
#   обьем сделки (сколько ценных бумаг было куплено)
#
# В ходе торгов цены сделок могут со временем расти и понижаться. Величина изменения цен называтея волатильностью.
# Например, если бумага №1 торговалась с ценами 11, 11, 12, 11, 12, 11, 11, 11 - то она мало волатильна.
# А если у бумаги №2 цены сделок были: 20, 15, 23, 56, 100, 50, 3, 10 - то такая бумага имеет большую волатильность.
# Волатильность можно считать разными способами, мы будем считать сильно упрощенным способом -
# отклонение в процентах от средней цены за торговую сессию:
#   средняя цена = (максимальная цена + минимальная цена) / 2
#   волатильность = ((максимальная цена - минимальная цена) / средняя цена) * 100%
# Например для бумаги №1:
#   average_price = (12 + 11) / 2 = 11.5
#   volatility = ((12 - 11) / average_price) * 100 = 8.7%
# Для бумаги №2:
#   average_price = (100 + 3) / 2 = 51.5
#   volatility = ((100 - 3) / average_price) * 100 = 188.34%
#
# В реальности волатильность рассчитывается так: https://goo.gl/VJNmmY
#
# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью.
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
# Подготовка исходных данных
# 1. Скачать файл https://drive.google.com/file/d/1l5sia-9c-t91iIPiGyBc1s9mQ8RgTNqb/view?usp=sharing
#       (обратите внимание на значок скачивания в правом верхнем углу,
#       см https://drive.google.com/file/d/1M6mW1jI2RdZhdSCEmlbFi5eoAXOR3u6G/view?usp=sharing)
# 2. Раззиповать средствами операционной системы содержимое архива
#       в папку python_base_source/lesson_012/trades
# 3. В каждом файле в папке trades содержится данные по сделакам по одному тикеру, разделенные запятыми.
#   Первая строка - название колонок:
#       SECID - тикер
#       TRADETIME - время сделки
#       PRICE - цена сделки
#       QUANTITY - количество бумаг в этой сделке
#   Все последующие строки в файле - данные о сделках
#
# Подсказка: нужно последовательно открывать каждый файл, вычитывать данные, высчитывать волатильность и запоминать.
# Вывод на консоль можно сделать только после обработки всех файлов.
#
# Для плавного перехода к мультипоточности, код оформить в обьектном стиле, используя следующий каркас
#
# class <Название класса>:
#
#     def __init__(self, <параметры>):
#         <сохранение параметров>
#
#     def run(self):
#         <обработка данных>
from abc import ABCMeta, abstractmethod
from lesson_012.python_snippets.utils import time_track
import re
import os


TICKER_ENTRY_RE = '\w{3}\d{1},\d{2}:\d{2}:\d{2},\d{1,}.\d{4},\d{1,}'
TITLE_STR = 'SECID,TRADETIME,PRICE,QUANTITY\n'


class AbstractReadTickerFileClass(metaclass=ABCMeta):
    """
    Абстрактный класс чтения файла тикера
    Используется паттерн: Шаблонный метод
    """
    def __init__(self, input_file_name='') -> None:
        """
        :param input_file_name: имя входного файла тикера
        """
        self.input_file_name = input_file_name
        self.path_root = os.path.dirname(__file__)
        self.ticker_price_list = []
        self.count_line_in_ticker = 0
        self.ticker_name = ''

    def read_input_file(self) -> bool:
        """
        Метод входит в шаблон:
        Чтение файла тикера в список self.ticker_price_list
        и вычисление количества записей self.count_line_in_ticker
        регулярка https://regex101.com/r/FKEeIw/1
        Принимаем в работу следующую схему: если заголовок неверный,
        значит это вообще не файл тикера, в рассчет его не берем,
        иначе, если строки битые - их игнорируем, если нормальные - считаем,
        если все строки битые - файл в рассчет не идет
        """
        return_result = True
        path_input_file = os.path.join(self.path_root, self.input_file_name)
        name = os.path.basename(self.input_file_name)
        if os.path.isfile(path_input_file):
            with open(self.input_file_name, mode='r', encoding='utf8') as input_file:
                title_str = input_file.readline()
                if title_str != TITLE_STR:
                    str_out_log_error = f'Файл {name} содержит ошибочный заголовок {title_str[:-1]}'
                    print(str_out_log_error)
                    print('Игнорируем его в рассчете!')
                    return False
                sec_id = None
                for line in input_file:
                    if re.match(TICKER_ENTRY_RE, line) is None:
                        str_out_log_error = f'В файле {name} содержится ошибочная строка {line[:-1]}'
                        print(str_out_log_error)
                        print('Игнорируем ее в рассчете!')
                    else:
                        sec_id, trade_time, price, quantity = line.split(',')
                        self.ticker_price_list.append(float(price))
                self.ticker_name = sec_id
                self.count_line_in_ticker = len(self.ticker_price_list)
                if self.count_line_in_ticker == 0:
                    return_result = False
        else:
            str_out_log_error = f'Файл {name} не найден в заданном каталоге!'
            print(str_out_log_error)
            return False
        return return_result

    def run(self) -> None:
        """
        Шаблонный метод - чтение файла тикера и рассчет по нему
        волатильности для этого тикера
        """
        if self.read_input_file():
            self.calculate_volatility()

    @abstractmethod
    def calculate_volatility(self) -> None:
        """
        Абстрактый метод - рассчет волатильности
        Определится у наследованного класса
        """
        pass


class VolatilityTicker(AbstractReadTickerFileClass):
    """
    Класс потомок с реализацией рассчета volatility
    """
    def __init__(self, input_file_name=''):
        """
        :param input_file_name: имя входного файла лога
        передаем в родительский класс через вызов конструктора
        """
        super().__init__(input_file_name=input_file_name, )
        self.sum_price = 0
        self.avg_price = 0
        self.volatility = 0

    def calculate_volatility(self):
        """
        Реализация метода рассчета volatility
        среднее значение рассичтываю по сумме всех записей
        """
        for price in self.ticker_price_list:
            self.sum_price += price
        self.avg_price = self.sum_price / self.count_line_in_ticker
        self.ticker_price_list.sort()
        self.volatility = (self.ticker_price_list[self.count_line_in_ticker - 1] -
                           self.ticker_price_list[0]) / self.avg_price * 100

    def get_volatility(self):
        return self.volatility

    def get_ticker_name(self):
        return self.ticker_name


class VolatilityTickerIterator(VolatilityTicker):
    """
    Для разнообразия, класс итератора для прохода по
    значениям списка цен тикеров из прочитанного файла input_file_name
    """
    def __init__(self, input_file_name=''):
        super().__init__(input_file_name=input_file_name)
        self.run()
        self.position_in_list = -1

    def __iter__(self):
        return self

    def __next__(self):
        """
        Выдача следующего значения
        """
        self.position_in_list += 1
        if self.position_in_list < self.count_line_in_ticker:
            return_str = self.ticker_price_list[self.position_in_list]
            return return_str
        else:
            raise StopIteration()


class VolatilityTickersOnDir:
    """
    Класс рассчета волатильности по группе файлов, находящихся в исходной папке
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

    def execute(self):
        """
        Проход в цикле по всем файлам исходной папки
        и создание объекта по классу VolatilityTicker на каждом шаге цикла
        с рассчетом в нем значений и явное удаление объекта после использования
        с последующим заполеним полученными значениями списков
        self.tickers_volatility_list
        self.zero_tickers_volatility_list
        """
        for dir_path, dir_names, file_names in os.walk(self.path_source):
            for file_name in file_names:
                path_input_file = os.path.join(self.path_source, file_name)
                tk = VolatilityTicker(input_file_name=path_input_file)
                tk.run()
                tick = tk.get_volatility()
                name_tick = tk.get_ticker_name()
                del tk
                if tick == 0.0 and name_tick is not None:
                    self.zero_tickers_volatility_list.append(name_tick)
                else:
                    self.tickers_volatility_list.append([tick, name_tick])
        self.tickers_volatility_list.sort()
        self.count_tickers_non_zero = len(self.tickers_volatility_list)
        self.zero_tickers_volatility_list.sort()


@time_track
def main():
    tickers = VolatilityTickersOnDir(source_dir='trades')
    tickers.execute()

    print('Максимальная волатильность:')
    for i in [2, 1, 0]:
        print(tickers.tickers_volatility_list[i][1], '--', '%.2f' % (tickers.tickers_volatility_list[i][0]))
    max_element = tickers.count_tickers_non_zero
    print('Минимальная волатильность:')
    for i in [max_element - 1, max_element - 2, max_element - 3]:
        print(tickers.tickers_volatility_list[i][1], '--', '%.2f' % (tickers.tickers_volatility_list[i][0]))
    print('Нулевая волатильность:')
    for ticker in tickers.zero_tickers_volatility_list:
        print(ticker, end=' ')
    print()


if __name__ == '__main__':
    main()

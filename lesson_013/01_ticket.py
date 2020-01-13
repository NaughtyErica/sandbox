# -*- coding: utf-8 -*-

# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда,
# куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru

import argparse
import os
from PIL import Image, ImageDraw, ImageFont, ImageColor
from abc import ABCMeta, abstractmethod

SOURCE_DIR = 'images'
FONT_NAME = "ofont_ru_Arial Cyr.ttf"
TICKET_TEMPLATE = "ticket_template.png"
TICKET_COMPLETE = "ticket_complete.png"


class AbstractMakerTicket(metaclass=ABCMeta):
    """
    Абстрактный класс заполенения шаблона билета
    Используется паттерн: Шаблонный метод
    """

    def __init__(self, first_name, last_name, city_from, city_to, dt_dep):
        """
        Определяем параметры для заполения шаблона билета и
        маршруты доступа к шрифту, шаблону и заполенному файлу билета
        :param first_name: Имя
        :param last_name: Фамилия
        :param city_from: Город отправления
        :param city_to: Город назначения
        :param dt_dep: дата вылета
        """
        self.first_name = first_name
        self.last_name = last_name
        self.city_from = city_from
        self.city_to = city_to
        self.dt_dep = dt_dep
        self.path_root = os.path.dirname(__file__)
        self.full_path_font = os.path.join(self.path_root,
                                           SOURCE_DIR, FONT_NAME)
        self.full_path_ticket_temp = os.path.join(self.path_root,
                                                  SOURCE_DIR,
                                                  TICKET_TEMPLATE)
        self.full_path_ticket_complete = os.path.join(self.path_root,
                                                      SOURCE_DIR,
                                                      TICKET_COMPLETE)
        self.image_ticket = Image.open(self.full_path_ticket_temp)

    def draw(self):
        """
        Рисуем билет и выводим на экран
        :return: None
        """
        draw = ImageDraw.Draw(self.image_ticket)
        font = ImageFont.truetype(self.full_path_font, size=13)
        draw.line((45, 141, 230, 141), width=1,
                  fill=ImageColor.colormap['white'])
        draw.text((45, 130), f"{self.first_name} {self.last_name}",
                  font=font, fill=ImageColor.colormap['black'])
        draw.line((45, 210, 200, 210), width=1,
                  fill=ImageColor.colormap['white'])
        draw.text((45, 197), self.city_from, font=font,
                  fill=ImageColor.colormap['black'])
        draw.line((45, 276, 200, 276), width=1,
                  fill=ImageColor.colormap['white'])
        draw.text((45, 265), self.city_to, font=font,
                  fill=ImageColor.colormap['black'])
        draw.line((286, 276, 330, 276), width=1,
                  fill=ImageColor.colormap['white'])
        draw.text((286, 265), self.dt_dep, font=font,
                  fill=ImageColor.colormap['black'])
        self.image_ticket.show()

    @abstractmethod
    def save(self):
        """
        Абстракный метод записи в файл готового билета
        определим в классе потомке
        """
        pass

    def execute(self):
        """
        Шаблонный метод исполения скрипта
        """
        self.draw()
        self.save()


class MakerTicket(AbstractMakerTicket):
    """
    Реализация заполнителя билета с помощью передачи
    параметров при создании объекта класса
    """

    def save(self):
        """
        Определяем непоследственную запись файла по адресу, определенном
        self.full_path_ticket_complete при инициализации
        """
        self.image_ticket.save(self.full_path_ticket_complete)
        print(f'Ticker complete saved at  {self.full_path_ticket_complete}')


# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля agrparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.
# Пример вызова скрипта
# python3 01_ticket.py -h
# python3 01_ticket.py ЮРИЙ КИРЕЕВ БИЙСК МОСКВА 01.07 --save_to=complete


class MakerTicketArgs(AbstractMakerTicket):
    """
    Реализация заполнителя билета с помощью парсинга командной строки
    """

    def __init__(self):
        """
        После парсинга коммандной строки передаем полученные
        параметры для заполения билета в родительский класс
        а полю self.save_to присваиваем значение, полученное из парсинга
        """
        parser = argparse.ArgumentParser(description='Completed Ticker')
        parser.add_argument('first_name', type=str, help='First name')
        parser.add_argument('last_name', type=str, help='Last name')
        parser.add_argument('city_from', type=str, help='City departure')
        parser.add_argument('city_to', type=str, help='City destination')
        parser.add_argument('dt_dep', type=str, help='Date departure')
        parser.add_argument('--save_to', type=str, default=None,
                            help='Default dir: None. \n '
                                 'When you specify a directory, '
                                 'the ticket will be saved to it')
        args = parser.parse_args()

        super().__init__(first_name=args.first_name,
                         last_name=args.last_name,
                         city_from=args.city_from,
                         city_to=args.city_to,
                         dt_dep=args.dt_dep)
        self.save_to = args.save_to

    def save(self):
        """
        Если был определен параметр целевая папка записи --save_to,
        то производим запись готового билета в указанную папку
        """
        if self.save_to:
            path_dir_for_save_ticket = os.path.join(self.path_root,
                                                    self.save_to)
            os.makedirs(path_dir_for_save_ticket)
            full_path_ticket_complete = os.path.join(self.path_root,
                                                     self.save_to,
                                                     TICKET_COMPLETE)
            self.image_ticket.save(full_path_ticket_complete)
            print(f'Ticker complete saved at  {full_path_ticket_complete}')


mt = MakerTicket(first_name='ЮРИЙ', last_name='КИРЕЕВ', city_from='БИЙСК',
                 city_to='МОСКВА', dt_dep='01.07')
mt.execute()

# mta = MakerTicketArgs()
# mta.execute()

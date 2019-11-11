# -*- coding: utf-8 -*-

# import os, time, shutil

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

import time
import os
import shutil
import random

#==================== первый рабочий вариант =====================
# source_dir = 'icons'
# target_dir = 'icons_by_year'
# year_dict = {}
#
# # Структура словаря для классификации файлов
# # {2010: {01:[file_name1,
# #             filename2,
# #             ...
# #            ],
# #        02:[file_name3,
# #            file_name4,
# #            ...
# #            ]
# #        ...
# #        }
# #  2011: {01:[file_name5,
# #             file_name6,
# #             ...
# #             ]
# #        }
# # }
#
# path_root = os.path.dirname(__file__)
# path_source = os.path.join(path_root, source_dir)
#
# for dir_path, dir_names, file_names in os.walk(path_source):
#     for name in file_names:
#         full_file_path = os.path.join(dir_path, name)
#         secs = os.path.getmtime(full_file_path)
#         file_time = time.gmtime(secs)
#         year = file_time.tm_year
#         month = file_time.tm_mon
#         if year in year_dict.keys():
#             if month in year_dict[year].keys():
#                 year_dict[year][month].append(full_file_path)
#             else:
#                 year_dict[year][month] = []
#         else:
#             year_dict[year] = {}
#
#
# path_target = os.path.join(path_root, target_dir)
# os.makedirs(path_target)
# for year in year_dict.keys():
#     path_target_year = os.path.join(path_target, str(year))
#     os.makedirs(path_target_year)
#     for month in year_dict[year].keys():
#         path_target_year_month = os.path.join(path_target_year, str(month).rjust(2, '0'))
#         os.makedirs(path_target_year_month)
#         for file in year_dict[year][month]:
#             shutil.copy2(file, path_target_year_month)

# ===============второй вариант в классах с шаблонным методом=============
from abc import ABCMeta, abstractmethod


class AbstractClassifierFilesClass(metaclass=ABCMeta):
    """
    Абстрактный класс составление классификатора по незаданным параметрам
    из исходной папки и копирования их в целевую папку, согласно
    выполенной классификации
    """
    def __init__(self, source_dir='', target_dir='') -> None:
        """
        :param source_dir: имя исходной папки с файлами для классификации
        :param target_dir: имя целевой папки для отклассифицированных файлов
        """
        self.classifier_dict = {}
        self.path_root = os.path.dirname(__file__)
        self.path_source = os.path.join(self.path_root, source_dir)
        self.path_target = os.path.join(self.path_root, target_dir)
        os.makedirs(self.path_target)

    @abstractmethod
    def make_classification(self) -> None:
        """
        Абстрактный метод составления классификации файлов
        """
        pass

    @abstractmethod
    def copy_files_to_new_structure(self) -> None:
        """
        Абстракный метод копирования файлов в целевую папку
        """
        pass

    def execute_copy(self):
        """
        Шаблонны метод, вызывающий два абстрактных метода
        """
        self.make_classification()
        self.copy_files_to_new_structure()


class ClassifierFilesYearMonth(AbstractClassifierFilesClass):

    def __init__(self, source_dir='', target_dir=''):
        super().__init__(source_dir=source_dir, target_dir=target_dir)
        self.count_source_files = 0
        self.count_target_files = 0
        print('Source path ->', self.path_source)
        print('Target path ->', self.path_target)

    def make_classification(self):
        """
        Метод классификации файлов из исходной папки по годам и месяцам их создания
        и заполение словаря, ключами которого являются года, а их значениями
        являются словари, ключами в которых являются месяца, а их значениями
        являются списки файлов
        """
        print('Classification files process begin ...')
        for dir_path, dir_names, file_names in os.walk(self.path_source):
            for name in file_names:
                full_file_path = os.path.join(dir_path, name)
                secs = os.path.getmtime(full_file_path)
                file_time = time.gmtime(secs)
                year = file_time.tm_year
                month = file_time.tm_mon
                if year not in self.classifier_dict.keys():
                    self.classifier_dict[year] = {}
                if month not in self.classifier_dict[year].keys():
                    self.classifier_dict[year][month] = []
                self.classifier_dict[year][month].append(full_file_path)
                self.count_source_files += 1
        print(self.count_source_files, 'files classified!')

    def copy_files_to_new_structure(self):
        """
        Прохождение по словарю-классификатору и копирование файлов
        в целевую папку
        """
        print('Copy files process begin ...')
        for year in self.classifier_dict.keys():
            path_target_year = os.path.join(self.path_target, str(year))
            os.makedirs(path_target_year)
            for month in self.classifier_dict[year].keys():
                path_target_year_month = os.path.join(path_target_year, str(month).rjust(2, '0'))
                os.makedirs(path_target_year_month)
                for file in self.classifier_dict[year][month]:
                    name_with_ext = os.path.basename(file)
                    path_target_year_month_file = os.path.join(path_target_year_month, name_with_ext)
                    if os.path.isfile(path_target_year_month_file):
                        index = name_with_ext.index('.')
                        name = name_with_ext[:index]
                        ext = name_with_ext[index:]
                        suffix = str(random.randint(10000, 99999))
                        new_name_with_ext = name + '_' + suffix + ext
                        path_target_year_month_new_name_with_ext = os.path.join(
                            path_target_year_month, new_name_with_ext)
                        shutil.copyfile(file, path_target_year_month_new_name_with_ext)
                        print(file, ' ===> ', path_target_year_month_new_name_with_ext)
                    else:
                        shutil.copy2(file, path_target_year_month)
                        print(file, ' ---> ', path_target_year_month)
                    self.count_target_files += 1
        print(self.count_target_files,  'files copied!')


file_ym = ClassifierFilesYearMonth(source_dir='icons', target_dir='icons_by_year')
file_ym.execute_copy()

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828

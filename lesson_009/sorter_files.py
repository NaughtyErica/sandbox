# -*- coding: utf-8 -*-

import time
import os
import shutil


from abc import ABCMeta, abstractmethod


class AbstractClassifierFilesClass(metaclass=ABCMeta):

    def __init__(self, source_dir='', target_dir='') -> None:
        self.classifier_dict = {}
        self.path_root = os.path.dirname(__file__)
        self.path_source = os.path.join(self.path_root, source_dir)
        self.path_target = os.path.join(self.path_root, target_dir)
        os.makedirs(self.path_target)
        
    @abstractmethod
    def make_classification(self) -> None:
        pass

    @abstractmethod
    def copy_files_to_new_structure(self) -> None:
        pass

    def execute_copy(self):
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
        print('Classification files process begin ...')
        for dir_path, dir_names, file_names in os.walk(self.path_source):
            for name in file_names:
                full_file_path = os.path.join(dir_path, name)
                secs = os.path.getmtime(full_file_path)
                file_time = time.gmtime(secs)
                year = file_time.tm_year
                month = file_time.tm_mon
                if year in self.classifier_dict.keys():
                    if month in self.classifier_dict[year].keys():
                        self.classifier_dict[year][month].append(full_file_path)
                        self.count_source_files += 1
                    else:
                        self.classifier_dict[year][month] = []
                else:
                    self.classifier_dict[year] = {}
        print(self.count_source_files, 'files classified!')

    def copy_files_to_new_structure(self):
        print('Copy files process begin ...')
        for year in self.classifier_dict.keys():
            path_target_year = os.path.join(self.path_target, str(year))
            os.makedirs(path_target_year)
            for month in self.classifier_dict[year].keys():
                path_target_year_month = os.path.join(path_target_year, str(month).rjust(2, '0'))
                os.makedirs(path_target_year_month)
                for file in self.classifier_dict[year][month]:
                    self.count_target_files += 1    
                    shutil.copy2(file, path_target_year_month)
                    print(file, ' ---> ', path_target_year_month)
        print(self.count_target_files,  'files copied!')


file_ym = ClassifierFilesYearMonth(source_dir='icons', target_dir='test')
file_ym.execute_copy()


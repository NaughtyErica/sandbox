# -*- coding: utf-8 -*-

# Сделать генератор текста на основе статистики
# Идея проста: подсчитаем какие буквы наиболее часто стоят рядом
# Точнее, подсчитаем как часто за буковой Х идет буква У, на основе некоего текста.
# После этого начнем с произвольной буквы и каждую следующую будем выбирать в зависимости от
# частоты её появления в статистике.
import zipfile

from random import randint


class Chatterer:
    analise_count = 4

    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = {}
        self.sequence = ''
        self.totals = {}
        self.stat_for_generate = {}

    def unzip(self):
        zip_file = zipfile.ZipFile(self.file_name, 'r')
        filename = ''
        for filename in zip_file.namelist():
            zip_file.extract(filename)
        self.file_name = filename

    def collect(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        self.sequence = ' ' * self.analise_count
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                self._collect_for_line(line=line[:-1])

    def _collect_for_line(self, line):
        for char in line:
            if self.sequence in self.stat:
                if char in self.stat[self.sequence]:
                    self.stat[self.sequence][char] += 1
                else:
                    self.stat[self.sequence][char] = 1
            else:
                self.stat[self.sequence] = {char: 1}
            self.sequence = self.sequence[1:] + char

    def prepare(self):
        for sequence, char_stat in self.stat.items():
            self.totals[sequence] = 0
            self.stat_for_generate[sequence] = []
            for char, count in char_stat.items():
                self.totals[sequence] += count
                self.stat_for_generate[sequence].append([count, char])
                self.stat_for_generate[sequence].sort(reverse=True)

    def chat(self, length_story=0, out_file_name=None):
        length_story = length_story
        printed = 0
        if out_file_name is not None:
            file = open(out_file_name, 'w', encoding='utf8')
        else:
            file = None

        sequence = ' ' * self.analise_count
        spaces_printed = 0
        while printed < length_story:
            char = self._get_char(char_stat=self.stat_for_generate[sequence],
                                  total=self.totals[sequence])
            if file:
                file.write(char)
            else:
                print(char, end='')
            if char == ' ':
                spaces_printed += 1
                if spaces_printed >= 10:
                    if file:
                        file.write('\n')
                    else:
                        print()
                    spaces_printed = 0
            printed += 1
            sequence = sequence[1:] + char
        if file:
            file.close()
    
    @staticmethod
    def _get_char(char_stat, total):
        dice = randint(1, total)
        pos = 0
        char = ''
        for count, char in char_stat:
            pos += count
            if dice <= pos:
                break
        return char


chatterer = Chatterer(file_name='voyna-i-mir.txt.zip')
chatterer.collect()
chatterer.prepare()
chatterer.chat(length_story=10000, out_file_name='out.txt')

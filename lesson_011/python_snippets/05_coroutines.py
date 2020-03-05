#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb


def reader(db):
    """Генератор. Читает строки таблицы user"""
    select = db.cursor()
    select.execute('SELECT surname, name, patronym FROM user')
    for row in select:
        yield row
    select.close()


def writer(db):
    """Сопрограмма. Пишет строки в таблицу user2"""
    insert = db.cursor()
    try:
        while True:
            row = (yield)
            try:
                insert.execute('INSERT INTO user2(surname, name, patronym) VALUES(%s, %s, %s)', row)
                db.commit()
            except:
                db.rollback()
    except GeneratorExit:
        insert.close()


def copy(db):
    """
    Подпрогрмма, использующая генератор и сопрограмму для копирования
    содержимого таблицы user в таблицу user2
    """
    write = writer(db)
    write.send(None)

    for row in reader(db):
        write.send(row)

    write.close()


db = MySQLdb.connect(user='user',
                     passwd='p4ssw0rd',
                     db='database',
                     charset='UTF8')

copy(db)

db.close()


# обёртка, которая позволит использовать сопрограммы вместе с оператором with.
# Класс-обёртка, который можно использовать для произвольных сопрограмм,
# не только для writer из примера:
class wrapper:
    def __init__(self, coro, *args, **kwargs):
        self.coro = coro(*args, **kwargs)

    def __enter__(self):
        self.coro.next()
        return self.coro

    def __exit__(self, type, value, traceback):
        self.coro.close()
        if value is None:
            return True
        return False

    def send(self, *args, **kwargs):
        return self.coro.send(*args, **kwargs)


# Переработанная функция копирования, использующая класс-обёртку и оператор with:
def copy_v1(db):
    """
    Подпрогрмма, использующая генератор и сопрограмму для копирования
    содержимого таблицы user в таблицу user2
    """
    with wrapper(writer, db) as write:
        for row in reader(db):
            write.send(row)

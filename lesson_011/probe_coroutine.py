lst1 = [1212, 3434, 4545, 45, 565, 565656, 6767]
lst2 = []


# Декоратор, для инициализации генератора  с помощью write.send(None)
def coroutine(f):
    def wrap(*args, **kwargs):
        gen = f(*args, **kwargs)
        gen.send(None)
        return gen
    return wrap


def reader(lst):
    """Генератор. Читает элементы списка lst"""
    for el in lst:
        yield el


@coroutine
def writer(lst):
    """Сопрограмма. Пишет элементы в списов lst"""
    try:
        while True:
            el = (yield)
            lst.append(el)
    except GeneratorExit:
        print('Копирование списка завершено!')


def copy_list(lst_in, lst_out):
    """
    Подпрогрмма, использующая генератор и сопрограмму для копирования
    содержимого списка lst_in в список lst_out
    """
    write = writer(lst=lst_out)
    # write.send(None)
    for elem in reader(lst=lst_in):
        print(f'Прочитан элемент {elem} из списка {lst_in}')
        write.send(elem)
        print(f'Записан элемент {elem} в список {lst_out}')
    write.close()


copy_list(lst_in=lst1, lst_out=lst2)






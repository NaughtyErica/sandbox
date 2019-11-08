from collections import OrderedDict
# Создаем словарь Ordered


dic = {'a': 14, 'd': 152, 'g': 162, 'j': 612, 'l': 212, 'w': 912, 'r': 112, 'c': 412}

list1 = sorted(dic.items(), key=lambda item: item[1], reverse=True)
# Игнорируем верхние 10%

# Выводим 100 слов из верхних 90%
print(list1)
print(dic.items())

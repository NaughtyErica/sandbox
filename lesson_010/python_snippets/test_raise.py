"""Комплексная задача.

Сложность: O(N).
"""

# Это пример кода, он может быть произвольно усложнен
# в рамках ограничений темы
#
# Требования:
#
# - в строках документации укажите исключения, если функция их возбуждает;
# - добавьте обработку исключений.


# Замените атрибуты словаря и др. на соответствующие своему варианту

def load_db():
    """Загрузить данные.

    Результат: list of dict.

    Сложность: O(1).
    """
    db = [
        {
            "name": "Иванов Иван",
            "birthday": "01/12/2000",
            "height": 170,
            "weight": 70.5,
            "car": True,
            "languages": ["С++", "Python"]
        },
        {
            "name": "Киреев Юрий",
            "birthday": "27/09/1964",
            "height": 195,
            "weight": 85.5,
            "car": True,
            "languages": ["Python"]
        },
        {
            "name": "Киреев Иван",
            "birthday": "28/04/1990",
            "height": 197,
            "weight": 80.5,
            "car": True,
            "languages": ["С++", "Java"]
        },
        {
            "name": "Киреев Толик",
            "birthday": "06/05/2006",
            "height": 185,
            "weight": 70.5,
            "car": False,
            "languages": ["Python"]
        },
        {
            "name": "Муравьев Слава",
            "birthday": "01/12/1990",
            "height": 185,
            "weight": 90.5,
            "car": True,
            "languages": ["PHP", "Go"]
        },
     ]
    return db


def print_employee(item):
    """Вывести объект 'item' на экран со всеми атрибутами.

    Сложность: O(1).
    """
    print("Имя: {}".format(item["name"]))
    print("Дата рождения: {}".format(item["birthday"]))
    print("Рост: {}".format(item["height"]))
    print("Вес: {}".format(item["weight"]))
    print("Наличие автомобиля: {}".format('Да' if item["car"] else 'Нет'))
    print("Имя: {}".format(item["languages"]))



def employees_filter(db, lang):
    """Вернуть отфильтрованную базу 'db' (список сотрудников), у которых
    в качестве языка программирования имеется 'lang'.

    Аргументы:
        - db (list of dict): база данных;
        - lang (str): язык программирования.

    Результат:
        - (list of dict): отфильтрованная база данных.

    Сложность: O(N).
    """
    # res - копия db, с сотрудниками, удовлетворяющими условию по языку
    res = []
    for item in db:
        if lang in item["languages"]:
            res.append(item)

    return res


def employee_employee_avg_height(db, younger_than):
    """Вернуть средний рост среди сотрудников 'db', у которых
    год рождения не менее 'younger_than'.

    Аргументы:
        - db (list of dict): база данных;
        - younger_than (int): минимальный год рождения.

    Результат:
        - (float): если такие сотрудники есть;
          (None): если таких сотрудников нет.

    Исключения:
        - ValueError: если кол-во найденных сотрудников равно 0.

    Сложность: O(N).
    """

    r_sum = 0
    r_col = 0
    for item in db:
        year = int(item["birthday"][-4:])
        if year >= younger_than:
            r_sum += item["height"]
            r_col += 1

    if r_col == 0:
        raise ValueError

    return r_sum / r_col


db = load_db()
while True:

    try:
        print("\n-----")
        print("Меню")
        print("-----")
        print("1. Список сотрудников.")
        print("2. Фильтр по языку программирования.")
        print("3. Средний рост сотрудников, моложе указанного г.р.")
        print("\nВыберите пункт меню или нажмите ENTER для выхода: ", end="")

        answer = input()

        if answer == "1":
            print("Содержимое базы данных ({}):".format(len(db)))
            for i, item in enumerate(db, start=1):
                print("{}.".format(i))
                print_employee(item)

        elif answer == "2":
            lang = input("Введите язык программирования: ")
            # "Нормализация" наименования языка на случай ошибки при вводе
            lang = lang.capitalize()

            res = employees_filter(db, lang)

            if len(res) > 0:
                print("Список сотрудников со знанием "
                      "языка программирования {} ({}):".format(lang, len(res)))
                for i, item in enumerate(res, start=1):
                    print("{}.".format(i))
                    print_employee(item)
            else:
                print("Таких сотрудников нет.")

        elif answer == "3":
            try:
                younger_than = int(input("Введите год рождения сотрудника: "))

                res = employee_employee_avg_height(db, younger_than)

                try:
                    print("Средний рост сотрудников, {} г.р. и моложе: "
                          "({:.1f}) см.".
                          format(younger_than, res))
                except ValueError:
                    print("Таких сотрудников нет.")
            except ValueError:
                print("Год рождения должен быть целым числом.")

        else:
            break

    except Exception as err:
        print("Произошла ошибка!")
        print("Тип:", type(err))
        print("Описание:", err)

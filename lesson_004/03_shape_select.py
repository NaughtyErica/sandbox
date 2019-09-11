# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

def polygon(point=sd.get_point(0, 0), angle=0, length=100, corner=3, color=sd.COLOR_YELLOW):
    first_vector = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
    first_vector.draw(color=color)
    next_vector = first_vector
    for i in range(corner - 1):
        if i == corner - 2:
            sd.line(start_point=next_vector.end_point, end_point=point, color=color)
        else:
            angle += int(360 / corner)
            next_vector = sd.get_vector(start_point=next_vector.end_point, angle=angle, length=length, width=1)
            next_vector.draw(color=color)


polygon_list = ["треугольник",
                "квадрат",
                "пятиугольник",
                "шестиугольник",
                "семиугольник",
                "восьмиугольник"
                ]
count_polygon = len(polygon_list)
while True:
    print('Возможные фигуры:')
    for i in range(count_polygon):
        print(i, ":", polygon_list[i])
    num_polygon = int(input('Введите желаемую фигуру:'))
    if num_polygon not in range(count_polygon):
        print('Вы ввели некорректный номер!', num_polygon)
    else:
        start_point = sd.get_point(300, 200)
        angle = 0
        length = 150
        polygon(point=start_point, angle=angle, length=length, corner=num_polygon + 3)
        sd.pause()
        break


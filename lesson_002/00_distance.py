#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов
from pprint import pprint

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = {}

moscow = sites['Moscow']
london = sites['London']
paris = sites['Paris']
moscow_london = round(((moscow[0] - london[0]) ** 2 + (moscow[1] - london[1]) ** 2) ** 0.5)
moscow_paris = round(((moscow[0] - paris[0]) ** 2 + (moscow[1] - paris[1]) ** 2) ** 0.5)
london_paris = round(((london[0] - paris[0]) ** 2 + (london[1] - paris[1]) ** 2) ** 0.5)

distances['Moscow'] = {}
distances['London'] = {}
distances['Paris'] = {}

distances['Moscow']['London'] = moscow_london
distances['Moscow']['Paris'] = moscow_paris
distances['London']['Moscow'] = moscow_london
distances['London']['Paris'] = london_paris
distances['Paris']['Moscow'] = moscow_paris
distances['Paris']['London'] = london_paris

# Форматированный вывод
# s_names = []
# for site_name in distances.keys():
#     s_names.append(site_name)
# i = 0
# for site_dist in distances.values():
#     print(s_names[i], '==>', site_dist)
#     i += 1

# Про .items() что-то пропустил!
# Вот так сильно проще:
for site_name, distance in distances.items():
    print(site_name, '=>', distance)

# print(distances)
# А вообще, есть для этого pprint()
pprint(distances)

# зачет!




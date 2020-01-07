# -*- coding: utf-8 -*-

# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru

import argparse
import os
from PIL import Image, ImageDraw, ImageFont, ImageColor


def make_ticket(fio, from_, to, date):
    path_root = os.path.dirname(__file__)
    source_dir = 'images'
    font = "ofont_ru_Arial Cyr.ttf"
    ticket_template = "ticket_template.png"
    ticket_complete = "ticket_complete.png"
    full_path_font = os.path.join(path_root, source_dir, font)
    full_path_ticket_temp = os.path.join(path_root, source_dir, ticket_template)
    full_path_ticket_complete = os.path.join(path_root, source_dir, ticket_complete)
    image_ticket = Image.open(full_path_ticket_temp)

    draw = ImageDraw.Draw(image_ticket)
    font = ImageFont.truetype(full_path_font, size=13)
    draw.line((45, 141, 230, 141), width=1, fill=ImageColor.colormap['white'])
    draw.text((45, 130), fio, font=font, fill=ImageColor.colormap['black'])
    draw.line((45, 210, 200, 210), width=1, fill=ImageColor.colormap['white'])
    draw.text((45, 197), from_, font=font, fill=ImageColor.colormap['black'])
    draw.line((45, 276, 200, 276), width=1, fill=ImageColor.colormap['white'])
    draw.text((45, 265), to, font=font, fill=ImageColor.colormap['black'])
    draw.line((286, 276, 330, 276), width=1, fill=ImageColor.colormap['white'])
    draw.text((286, 265), date, font=font, fill=ImageColor.colormap['black'])
    image_ticket.show()
    image_ticket.save(full_path_ticket_complete)
    print(f'Ticker complete saved at  {full_path_ticket_complete}')

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


def make_ticket_args():
    parser = argparse.ArgumentParser(description='Completed Ticker')
    parser.add_argument('first_name', type=str, help='First name')
    parser.add_argument('last_name', type=str, help='Last name')
    parser.add_argument('city_from', type=str, help='City departure')
    parser.add_argument('city_to', type=str, help='City destination')
    parser.add_argument('dt_dep', type=str, help='Date departure')
    parser.add_argument('--save_to', type=str, default=None,
                        help='Default dir: None. \n When you specify a directory, the ticket will be saved to it')
    args = parser.parse_args()
    path_root = os.path.dirname(__file__)
    source_dir = 'images'
    font = "ofont_ru_Arial Cyr.ttf"
    ticket_template = "ticket_template.png"
    ticket_complete = "ticket_complete.png"
    full_path_font = os.path.join(path_root, source_dir, font)
    full_path_ticket_temp = os.path.join(path_root, source_dir, ticket_template)

    image_ticket = Image.open(full_path_ticket_temp)
    draw = ImageDraw.Draw(image_ticket)
    font = ImageFont.truetype(full_path_font, size=13)
    draw.line((45, 141, 230, 141), width=1, fill=ImageColor.colormap['white'])
    draw.text((45, 130), f"{args.first_name} {args.last_name}", font=font, fill=ImageColor.colormap['black'])
    draw.line((45, 210, 200, 210), width=1, fill=ImageColor.colormap['white'])
    draw.text((45, 197), args.city_from, font=font, fill=ImageColor.colormap['black'])
    draw.line((45, 276, 200, 276), width=1, fill=ImageColor.colormap['white'])
    draw.text((45, 265), args.city_to, font=font, fill=ImageColor.colormap['black'])
    draw.line((286, 276, 330, 276), width=1, fill=ImageColor.colormap['white'])
    draw.text((286, 265), args.dt_dep, font=font, fill=ImageColor.colormap['black'])
    image_ticket.show()
    if args.save_to:
        path_dir_for_save_ticket = os.path.join(path_root, args.save_to)
        os.makedirs(path_dir_for_save_ticket)
        full_path_ticket_complete = os.path.join(path_root, args.save_to, ticket_complete)
        image_ticket.save(full_path_ticket_complete)
        print(f'Ticker complete saved at  {full_path_ticket_complete}')


make_ticket(fio='ЮРИЙ КИРЕЕВ', from_='БИЙСК', to='МОСКВА', date='01.07')
# make_ticket_args()

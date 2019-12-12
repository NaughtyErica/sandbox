# -*- coding: utf-8 -*-

# pip install -r requirements.txt
from astrobox.space_field import SpaceField
from kireev import UrikDrone


class DiplomaSpaceField(SpaceField):

    def __init__(self, *args, **kwargs):
        self.table_logistic = []
        self.table_content_asteroids = []
        self.table_distance_form_mather_ship = []
        self.count_asteroids = 0
        super(DiplomaSpaceField, self).__init__(*args, **kwargs)

    def calculate_first_target(self):
        """
        Рассчитаем номер первой цели, как самый дальний астероид от базы
        Вызывается один раз при рождении дрона
        """
        self.count_asteroids = len(self.asteroids)
        x, y = self.motherships[0].coord.x, self.motherships[0].coord.y
        for i in range(self.count_asteroids):
            distance = int(((x - self.asteroids[i].coord.x) ** 2 + (y - self.asteroids[i].coord.y) ** 2) ** 0.5)
            self.table_distance_form_mather_ship.append([distance, i])
        self.table_distance_form_mather_ship.sort(reverse=True)
        first_num_asteroid = self.table_distance_form_mather_ship[0][1]
        return first_num_asteroid

    def calculate_nearest_non_empty_asteroid(self, num_aster_for_calc=0):
        """
        Заполняем таблицу логистики для выбора порядка облёта астероидов
        и отдаем самый близкий не пустой в процессе выбора цели при неполном
        трюме после загрузки на очередном астероиде
        """
        num_asteroid = -1
        for asteroid in self.asteroids:
            num_asteroid += 1
            self.table_content_asteroids.append([num_asteroid,
                                                 asteroid.coord.x,
                                                 asteroid.coord.y,
                                                 asteroid.payload
                                                 ])
        n = num_aster_for_calc
        x, y = self.asteroids[n].coord.x, self.asteroids[n].coord.y
        self.table_logistic = []
        for i in range(self.count_asteroids):
            distance = int(((x - self.asteroids[i].coord.x) ** 2 + (y - self.asteroids[i].coord.y) ** 2) ** 0.5)
            payload = self.asteroids[i].payload
            if payload > 0 and distance > 0:
                self.table_logistic.append([distance, payload, i])
        self.table_logistic.sort()
        print(self.table_logistic)
        return self.table_logistic[0][2]


if __name__ == '__main__':
    scene_1 = DiplomaSpaceField(speed=3,
                                asteroids_count=5,
                                can_fight=True
                                )
    d = UrikDrone()
    scene_1.go()
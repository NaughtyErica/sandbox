# -*- coding: utf-8 -*-
from random import randint
from astrobox.core import Drone
from robogame_engine.constants import GAME_OVER
from python_base_diploma.management import LogisticOnField


class UrikDrone(Drone):
    my_team = []

    def __init__(self):
        super().__init__()
        self.number_visited_asteroid = 0
        self.count_asteroids = 0
        self.count_visited_asteroids = 1
        self.table_logistic = []
        self.table_content_asteroids = []
        self.table_distance_form_mather_ship = []
        self.count_asteroids = 0

    def on_born(self):
        self.count_asteroids = len(self.asteroids)
        self.number_visited_asteroid = randint(0, self.count_asteroids - 1)
        self.target = self.asteroids[self.number_visited_asteroid]
        # print(f'Первая цель {self.target.coord}. Астероидов всего {self.count_asteroids}. '
        #       f'Летим на астероид номер {self.number_visited_asteroid}')
        self.move_at(self.target)
        self.my_team.append(self)

    # Найти ближайший непустой
    def _get_my_asteroid(self):
        return_aster = None
        for aster in self.asteroids:
            if aster.cargo.payload > 0:
                return_aster = aster
        if return_aster is not None:
            return return_aster
        else:
            return self.asteroids[randint(0, self.count_asteroids - 1)]

    def on_stop_at_asteroid(self, asteroid):
        self.load_from(asteroid)

    def on_load_complete(self):
        # print(f'Загрузили в трюм {self.payload}, свободного места в трюме {self.free_space}')
        if self.free_space > 0:
            self.target = self._get_my_asteroid()
            # print(f'Получена новая цель  =====>> {self.target.coord} астероид номер {self.number_visited_asteroid}')
            self.move_at(self.target)
        else:
            # print(f'На {self.target.coord} осталось элериума {self.target.payload}. Летим на базу')
            self.move_at(self.my_mothership)

    def on_stop_at_mothership(self, mothership):
        self.unload_to(mothership)

    def on_unload_complete(self):
        # print(f'Разгрузились на базе. В трюме {self.payload}. '
        #       f'На покинутом астероиде № {self.number_visited_asteroid} '
        #       f'элериума {self.target.payload}')
        # print(f'В трюме {self.payload}. Цель {self.target} - астероид номер {self.number_visited_asteroid}')

        # if self.target.payload == 0 and self.count_visited_asteroids == self.count_asteroids:
        #     self.scene.parent_conn.send(GAME_OVER)
        # else:
        self.target = self._get_my_asteroid()
        self.move_at(self.target)

    def on_wake_up(self):
        print('Шляпа!')
        # self.scene.parent_conn.send(GAME_OVER)

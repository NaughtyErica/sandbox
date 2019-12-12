# -*- coding: utf-8 -*-

from astrobox.core import Drone
from robogame_engine.constants import GAME_OVER


class UrikDrone(Drone):
    my_team = []

    def __init__(self):
        super(UrikDrone, self).__init__()
        self.number_visited_asteroid = 0
        self.count_asteroids = 0
        self.count_visited_asteroids = 1

    def on_born(self):
        self.count_asteroids = len(self.asteroids)
        self.number_visited_asteroid = self.scene.calculate_first_target()
        self.target = self.asteroids[self.number_visited_asteroid]
        print(f'Первая цель {self.target.coord}. Астероидов всего {self.count_asteroids}. '
              f'Летим на астероид номер {self.number_visited_asteroid}')
        self.move_at(self.target)
        self.my_team.append(self)

    def _get_my_asteroid(self):
        new_number_target = self.scene.calculate_nearest_non_empty_asteroid(num_aster_for_calc=
                                                                            self.number_visited_asteroid)
        self.number_visited_asteroid = new_number_target
        self.count_visited_asteroids += 1
        return self.asteroids[self.number_visited_asteroid]

    def on_stop_at_asteroid(self, asteroid):
        self.load_from(asteroid)

    def on_load_complete(self):
        print(f'Загрузили в трюм {self.payload}, свободного места в трюме {self.free_space}')
        if self.free_space > 0 and self.count_visited_asteroids < self.count_asteroids:
            self.target = self._get_my_asteroid()
            print(f'Получена новая цель  =====>> {self.target.coord} астероид номер {self.number_visited_asteroid}')
            self.move_at(self.target)
        else:
            print(f'На {self.target.coord} осталось элериума {self.target.payload}. Летим на базу')
            self.move_at(self.my_mothership)

    def on_stop_at_mothership(self, mothership):
        self.unload_to(mothership)

    def on_unload_complete(self):
        print(f'Разгрузились на базе. В трюме {self.payload}. '
              f'На покинутом астероиде № {self.number_visited_asteroid} '
              f'элериума {self.target.payload}')
        print(f'В трюме {self.payload}. Цель {self.target} - астероид номер {self.number_visited_asteroid}')
        if self.target.payload == 0 and self.count_visited_asteroids == self.count_asteroids:
            self.scene.parent_conn.send(GAME_OVER)
        else:
            self.move_at(self.target)

    def on_wake_up(self):
        self.scene.parent_conn.send(GAME_OVER)

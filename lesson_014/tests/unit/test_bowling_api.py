# -*- coding: utf-8 -*-
# Запуск тестов командой pytest -v -k test_bot.py

from bowling import get_score
import pytest


@pytest.mark.smoke
def test_get_score_function_result():
    res = get_score(game_result='Х4/34')
    assert res == 42


# @pytest.mark.parametrize(argnames="wind_deg", argvalues=[315, 270, 225, 180, 135, 90, 45, 0])
# def test_wind_direct(wind_deg):
#     direct = wg.get_wind_direction(wind_deg=wind_deg)
#     assert WIND_DIRECT_TEST.pop() == direct



# -*- coding: utf-8 -*-
# Запуск тестов командой pytest -v -k test_bowling_api.py находясь в текущем каталоге unit

from bowling import *
import pytest


GAME_BAD_RESULT_LIST = [
                        '9999',
                        'XYI',
                        '-0-0',
                       ]


def test_get_score_function_bad0_result():
    with pytest.raises(ErrorSumFrame) as exc_info:
        get_score(game_result=GAME_BAD_RESULT_LIST[0])
    assert "Некорректное" in str(exc_info.value)


def test_get_score_function_bad1_result():
    with pytest.raises(ErrorInputData) as exc_info:
        get_score(game_result=GAME_BAD_RESULT_LIST[1])
    assert "Недопустимое" in str(exc_info.value)


def test_get_score_function_bad2_result():
    with pytest.raises(ErrorInputData) as exc_info:
        get_score(game_result=GAME_BAD_RESULT_LIST[2])
    assert "Недопустимое" in str(exc_info.value)

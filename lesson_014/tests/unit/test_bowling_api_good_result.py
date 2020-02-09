# -*- coding: utf-8 -*-
# Запуск тестов командой pytest -v -k test_bowling_api.py находясь в текущем каталоге unit

from bowling import get_score
import pytest
from pytest import approx

GAME_GOOD_RESULT_LIST = [
                        ('X4/34-45-237/X-2x', 93),
                        ('525/XX5--4XX6181X', 147),
                        ('71XX27-56/519/12XX', 141),
                        ('24X-35-1/X35-9X17X', 134),
                        ('16-99/X12XX6-8/X41', 140),
                        ('8/9/1462X9--5X7-6/', 119),
                        ('------------', 0)
                        ]


@pytest.mark.parametrize(argnames="game_result, score", argvalues=GAME_GOOD_RESULT_LIST)
def test_get_score_function_good_result(game_result, score):
    res = get_score(game_result=game_result)
    assert res == approx(expected=score)

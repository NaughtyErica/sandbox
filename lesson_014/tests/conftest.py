import time
import pytest


@pytest.fixture(autouse=True, scope='session')
def footer_session_scope():
    """Авто-фикстура: Отчет о времени начала и конца сессии"""
    yield
    now = time.time()
    print('\n-----------------')
    print('Окончание теста : {}'.format(time.strftime('%d %b %X', time.localtime(now))))
    print('-----------------')


@pytest.fixture(autouse=True)
def footer_function_scope():
    """Авто-фикстура: Сообщает продолжительность теста после каждой функции."""
    start = time.time()
    yield
    stop = time.time()
    delta = stop - start
    print('\nДлительность теста : {:0.3} секунд'.format(delta))

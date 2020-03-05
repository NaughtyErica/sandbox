"""
Этот способ отлично подходит для повышения скорости относительно небольших списков.
С очень большими списками он может вызвать проблемы при работе, поскольку все вводы/выводы кэшируются,
пока функция находится в области видимости, что требует большого количества памяти для хранения значений.
"""


def memoize(func):
    """ Memoization decorator for functions taking one or more arguments. """

    class MemoDict(dict):
        def __init__(self, input_func):
            super().__init__()
            self.func = input_func

        def __call__(self, *args):
            return self[args]

        def __missing__(self, key):
            ret = self[key] = self.func(*key)
            return ret

    return MemoDict(func)


# Инициализация переменной вызова глобальной функции
funcRuns = 0


# Упаковка функции во враппере мемоизации
@memoize
def f(arg):
    global funcRuns
    # Увеличение funcRuns при каждом запуске функции
    funcRuns += 1
    result = arg**2
    print(f"result from {arg} calculate")
    return result


# Инициализация списка чисел

nums = [5, 40, 25, 30, 40, 40, 25, 30, 5]

# Запуск спискового включения с двумя вызовами f(x) на каждую итерацию
#   с 6 элементами в списке и 2 вызовами за итерацию, что
#   приведет к 12 выполнениям функций.
# new_list = [f(x) for x in nums if f(x) > 100]
new_list = []
for x in nums:
    if f(x) > 100:
        new_list.append(f(x))


print(new_list)
# Запуск номера журнала f(x)
print(f"Count of calling function f(x) ==>> {funcRuns}")

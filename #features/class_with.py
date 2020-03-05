from random import randint
from contextlib import contextmanager
import time


# class DemoContextManager:
#     def __init__(self, label):
#         self.label = label
#
#     def __enter__(self):
#         print(f"--------------{self.label}--------------------")
#         self.start = time.time()
#
#     def __exit__(self, exc_ty, exc_val, exc_tb):
#         self.end = time.time()
#         self.period = self.end - self.start
#         print(f"Длительность вычислений {self.period}")
#         print("=============================================")
#
#
# rand_value_lst = [randint(1, 1000000) for value in range(20000)]
#
# with DemoContextManager('Сортировка'):
#     rand_value_lst.sort()


@contextmanager
def ctx_mng(label):
    start = time.time()
    print(f"--------------{label}---------------------")
    try:
        yield
    finally:
        end = time.time()
        period = end - start
        print(f"Длительность вычислений {period}")
        print("=============================================")


rand_value_lst = [randint(1, 1000000) for value in range(20000)]
with ctx_mng('Сортировка'):
    rand_value_lst.sort()

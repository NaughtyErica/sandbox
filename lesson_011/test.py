source_list = [1, 3, 5, 23, 45, 67, 78]
def func_multiply_two(n=1):
    return n * 2
def func_square(m=1):
    return m ** 2


# императивный вариант
target = []  # создать пустой список
for item in source_list:  # для каждого элемента исходного списка
    trans1 = func_multiply_two(item)  # применить функцию G()
    trans2 = func_square(trans1)  # применить функцию F()
    target.append(trans2)  # добавить преобразованный элемент в список
print('null')
print(target)

# функциональный вариант
print('first')


def compose_func_first(f1, f2):
    def fabrica(x):
        return f1(f2(x))
    return fabrica


target = map(compose_func_first(func_square, func_multiply_two), source_list)
for item in target:
    print(item)


print('second')
compose_func = lambda x: (x * 2) ** 2
for item in source_list:
    print(compose_func(item))

print('third')
target = map(compose_func, source_list)
for res in target:
    print(res)

print('fourth')


compose2 = lambda func_2, func_1: lambda x: func_2(func_1(x))

target = map(compose2(func_square, func_multiply_two), source_list)
for item in target:
    print(item)



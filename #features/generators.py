import os

num = [1, 4, -5, 10, -7, 2, 3, -1]
filtered_and_squared = []

for number in num:
    if number > 0:
        filtered_and_squared.append(number ** 2)
print(filtered_and_squared)


num = [1, 4, -5, 10, -7, 2, 3, -1]
filtered_and_squared = map(lambda x: x ** 2, filter(lambda x: x > 0, num))
print(filtered_and_squared)


num = [1, 4, -5, 10, -7, 2, 3, -1]
filtered_and_squared = [x**2 for x in num if x > 0]
print(filtered_and_squared)


num = [1, 4, -5, 10, -7, 2, 3, -1]
filtered_and_squared = (x**2 for x in num if x > 0 )
print(filtered_and_squared)

for item in filtered_and_squared:
    print(item)

# ---------------------------------------------
num = [1, 4, -5, 10, -7, 2, 3, -1]


def square_generator(optional_parameter):
    return (x ** 2 for x in num if x > optional_parameter)


print(square_generator(0))
for k in square_generator(0):
    print(k)
g = list(square_generator(0))
print(g)

# -------------------------------------
a_list = ['a1', 'a2', 'a3']
b_list = ['1', '2', '3']

for a, b in zip(a_list, b_list):
    print(a, b)

# ---------------------------------------


def tree(top):
    for path, names, f_names in os.walk(top):
        for f_name in f_names:
            yield os.path.join(path, f_name)


for name in tree('/home/urik/Downloads'):
    print(name)

# -*- coding: utf-8 -*-

# Написать декоратор, который будет логировать (записывать в лог файл)
# ошибки из декорируемой функции и выбрасывать их дальше.
#
# Имя файла лога - function_errors.log
# Формат лога: <имя функции> <параметры вызова> <тип ошибки> <текст ошибки>
# Лог файл открывать каждый раз при ошибке в режиме 'a'


def log_errors(func):
    def decorated_func(*args, **kwargs):
        result = None
        try:
            result = func(*args, **kwargs)
        except Exception as exc:
            log_str = f'{func.__name__} {args} {kwargs} {str(type(exc))[7:-1]} {exc} \n'
            output_file = open('function_errors.log', mode='a', encoding='utf8')
            output_file.write(log_str)
            output_file.close()
        return result
    return decorated_func


# Проверить работу на следующих функциях
@log_errors
def perky(param):
    return param / 0


@log_errors
def check_line(line):
    name, email, age = line.split(' ')
    if not name.isalpha():
        raise ValueError("it's not a name")
    if '@' not in email or '.' not in email:
        raise ValueError("it's not a email")
    if not 10 <= int(age) <= 99:
        raise ValueError('Age not in 10..99 range')


lines = [
    'Ярослав bxh@ya.ru 600',
    'Земфира tslzp@mail.ru 52',
    'Тролль nsocnzas.mail.ru 82',
    'Джигурда wqxq@gmail.com 29',
    'Земфира 86',
    'Равшан wmsuuzsxi@mail.ru 35',
]
for line in lines:
    try:
        check_line(line)
    except Exception as exc:
        print(f'Invalid format: {exc}')
perky(param=42)


# Усложненное задание (делать по желанию).
# Написать декоратор с параметром - именем файла
#
# @log_errors('function_errors.log')
# def func():
#     pass
#

def log_errors_with_file_name(log_file_name=None):
    if log_file_name:
        output_file_name = log_file_name
    else:
        output_file_name = 'function_errors.log'

    def log_errors_dec(func):
        def decorated_func(*args, **kwargs):
            result = None
            try:
                result = func(*args, **kwargs)
            except Exception as exc:
                log_str = f'{func.__name__} {args} {kwargs} {str(type(exc))[7:-1]} {exc} \n'
                output_file = open(output_file_name, mode='a', encoding='utf8')
                output_file.write(log_str)
                output_file.close()
            return result
        return decorated_func
    return log_errors_dec


@log_errors_with_file_name(log_file_name='123.txt')
def perky(param):
    return param / 0


perky(param=42)

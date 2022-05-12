# Реализовать декоратор в котором нужно подсчитать кол-во вызовов декорированной функции в процессе выполнения кода.
# Выгрузить статистику подсчета в файл debug.log в формате: Название функции, кол-во вызовов, дата-время последнего выполнения
# Пример:
# render, 10,  12.05.2022 12:00
# show,    5,  12.05.2022 12:02
# render, 15,  12.05.2022 12:07
#
# Декоратор должен применяться для различных функций с переменным числом аргументов.
# Статистику вызовов необходимо записывать в файл при каждом запуске скрипта.

import sys
from datetime import datetime

current_time = datetime.now()


def decorator_counter(func):
    print('Идет сбор данных...')

    def wrapper(*args, **kwargs):
        wrapper.count += 1
        return func(*args, **kwargs)

    wrapper.count = 0
    return wrapper


@decorator_counter
def render(text):
    text.upper()
    # print(f'Это функция render выводит {text.upper()}')


render('hi')
render('hello')
render('world')
print(f'Функция render выводилась {render.count} раза, последний раз: {current_time} , данные записанны в файл debug.log')


@decorator_counter
def show(text):
    text.capitalize
    # print(f'Это функция show выводит {text.capitalize()}')


show('hello')
show('world')
show('hi')
show('good')
show('morning')
print(f'Функция show выводилась {show.count} раза, последний раз: {current_time} , данные записанны в файл debug.log')

original_stdout = sys.stdout
with open('debug.log', 'w', encoding='UTF-8') as f:
    sys.stdout = f
    print(f'Функция render выводилась {render.count} раза, последний раз: {current_time}')
    print(f'Функция show выводилась {show.count} раза, последний раз: {current_time}')
    sys.stdout = original_stdout

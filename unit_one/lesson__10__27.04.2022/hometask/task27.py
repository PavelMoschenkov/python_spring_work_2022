# Для игры "Отгадай число от 0 до 100" реализованной на занятии 4 homework/task3
# написать Save Game по следующему сценарию:
# В запущенной игре по нажатию клавиши S появляется вывод:
# 1. Продолжить
# 2. Сохранить игру
#
# При выборе пункта 1. игра продолжается.
# При выборе пункта 2. пользователю предлагается ввести название для
# сохранения, после чего нужно сделать сериализацию состояния игры.
# Законсервировать все объекты которые отвечают за состоянии игры в файл
# game_dump.pkl   Сериализацию и десериализацию сделать на базе библиотеки pickle.
#
# При старте игры пользователю должен предлагатся выбор
# 1. Новая игра
# 2. Восстановить игру
# При выборе 1. начинается новая игра.
# При выборе 2. пользователю выводится список всех сохраненных игр(происходит десериализация).
# Из них он выберает нужную, после чего загружается состояние игры на момент сохранения.


import pickle
import random
save_dict = {} #словарь для сохранений

print("Добро пожаловать в игру угадай число!")
print("Что вы хотите сделать?")
print("1. Новая игра", '\n', "2. Восстановить игру")
choice = int(input('Введите 1 или 2:'))
if choice == 1: #если новая игра, просто запускаем обычную игру, но с возможностью ввести s и сохранится
    x = random.randint(0, 100)
    error = 0
    while error <= 10:
        number = input("Введите число от 1 до 100: ")
        if number in ['s', 'S', 'ы', 'Ы']: #если ввели что угодно из того что в массиве переходим в сохранялку
            print("Что вы хотите сделать?")
            print("1. Продолжить", '\n', "2. Сохранить")
            to_do = int(input('Введите 1 или 2:'))
            if to_do == 1:
                continue #пропускаем ход и идем дальше
            if to_do == 2:
                name = input('Введите название для сохранения')
                save_dict[name] = error, x #сохраняем колво ошибок и загаданное число
                f_wr = open("game_dump.pkl", "wb") #открываем файл с целью записать (wb)
                pickle.dump(save_dict, f_wr)  #сохраняем в файл
                f_wr.close() #закрываем
        else:
            number = int(number) #играем как обычно
            if number < x:
                print("Твое число меньше.")
            if number > x:
                print("Твое число больше")
            if number == x:
                print("Вы угадали")
                break
            error += 1
    else:
        print("ТЫ не угадал! Я загадал ", x)

if choice == 2:
    f_op = open("game_dump.pkl", "rb") #открываем файл
    save_dict = pickle.load(f_op) #грузим словарь из сохранений
    print('Ваши сохранения: ')
    print(*save_dict.keys()) #* - чтобы отражался текст а не массив
    name = input('Введите название сохранения ')
    while name not in save_dict.keys(): #пока название неправильное
        name = input('Неверное название, введите другое: ')
    error = save_dict[name][0] #вписываем сохраненные до этого ошибки и загаданное число, далее обычная игра
    x = save_dict[name][1]
    while error <= 10:
        number = input("Введите число от 1 до 100: ")
        if number in ['s', 'S', 'ы', 'Ы']:
            print("Что вы хотите сделать?")
            print("1. Продолжить", '\n', "2. Сохранить")
            to_do = int(input('Введите 1 или 2:'))
            if to_do == 1:
                continue
            if to_do == 2:
                name = input('Введите название для сохранения')
                save_dict[name] = error, x
                f_wr = open("game_dump.pkl", "wb")
                pickle.dump(save_dict, f_wr)
                f_wr.close()
        else:
            number = int(number)
            if number < x:
                print("Твое число меньше.")
            if number > x:
                print("Твое число больше")
            if number == x:
                print("Вы угадали")
                break
            error += 1
    else:
        print("ТЫ не угадал! Я загадал ", x)
    f_op.close()
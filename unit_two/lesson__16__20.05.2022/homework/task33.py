#  Написать авторизацию пользователя в систему.
# Приложение в начале должно предлагать меню
# 1. Вход
# 2. Регистрация
#
#
# 1. При выборе пункта "Вход" пользователю необходимо ввести
# логин и пароль, поэтапно.
# login: _________
# password: ________
# При вводе данных авторизации, система проверяет есть ли данный
# пользователь в БД (логин) если нет то предлагает зарегистрироваться.
# Если есть и пароли совпадают, то происходит вход в систему. Пользователю показывается
# приглашение вида "Добро пожаловать Вася Пупкин!" и выпадает меню
# выбора билетов для тестирования(пока заглушка).
#
# 2. При выборе "Регистрация" пользователю необходимо ввести новый
# логин, пароль, фио, почту, телефон, группу. После система заводит
# запись в БД если пользователя под данным логином нет. Если такой пользователь
# уже существует то программа выдает об этом сообщение. Пароль необходимо хранить в БД
# в виде хеша + соль.
#
# По хешированию прочитать статью
# https://pythonist.ru/heshirovanie-parolej-v-python-tutorial-po-bcrypt-s-primerami/
# для хеширования пароля воспользоваться библиотекой bcrypt



import bcrypt
import psycopg

with psycopg.connect("dbname=testsystem user=testsystem password=12345") as conn: # Подключаемся к БД
    with conn.cursor() as cur:
        print('Вы вошли в матрицу!')
        print("""Выберите из меню: 
                    1. Вход
                    2. Регистрация""")
        vvod = int(input("Введите цифру изменю: "))

        cur.execute("""SELECT login FROM profile;""")
        profile1 = list(sum(cur.fetchall(), ())) # получаем спискок имеющихся логинов в БД

        if vvod == 1:
            login = str(input("Ведите логин: "))
            password = str(input("Введите пароль: "))
            if login in profile1: # ищем есть ли логин в БД
                print(f'{login}, добро пожаловать в занимательные тесты с Шелдоном Купером!')
                print(f'Выберите тему теста:{input()} ')

            else:
                print('Вы не заригестрированны начните заново и выберите цифру 2')
                print("""Выберите из меню: 
                    1. Вход
                    2. Регистрация""")
                vvod1 = int(input("Введите цифру изменю: "))


    if vvod or vvod1  == 2:
        new_login = input('Введите Логин: ')
        new_pass = input('Введите пароль: ')
        surname = input('Введите Фамилию: ')
        name = input('Введите Имя: ')
        patronymic = input('Введите Отчество: ')
        age = input('Введите Возраст: ')
        id_user = int(input('Введите ID юзера: '))
        id_profile  = int(input('Введите ID профайла: '))
        avatar = '123444'
        dt_reg = '2022-05-24 15:30:25'
        dt_last_login = '2022-05-24 15:30:25'
        dt_create = '2022-05-24 15:30:25'
        status = True
        hashAndSalt = bcrypt.hashpw(new_pass.encode(), bcrypt.gensalt())
        hashAndSalt = hashAndSalt.decode('utf-8')
        cur.execute("SELECT login FROM profile")

        if new_login in profile1:
            print('Такой пользователь уже существует!')
            # заносим в базу
        else:
            cur.execute (f"""
                        INSERT INTO users (id_user, surname, name, patronymic, age, dt_create, status)
                        VALUES  ({id_user}, '{surname}', '{name}', '{patronymic}',{age}, '{dt_create}', {status});
                        """)

            cur.execute (f"""
                        INSERT INTO profile (id_profile, id_user, login, password, avatar, dt_reg, dt_last_login, status)
                        VALUES  ({id_profile}, {id_user}, '{new_login}', '{hashAndSalt}', '{avatar}', '{dt_reg}', '{dt_last_login}', {status});
                        """)

            print('Поздравляем вы успешно зарегистрировались!')








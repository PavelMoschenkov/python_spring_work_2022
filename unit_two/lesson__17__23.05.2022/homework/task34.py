# Реализовать классы DB и Profile

import psycopg


class DB:
    # '''Данный класс содержит конструктор и метод get_connect. В конструкторе инициализируются переменные
    #  (атрибуты доступа к БД) . Метод возвращает соединение.'''

    def __init__(self, dbname, user, password):
        self.dbname = dbname
        self.user = user
        self.password = password

    def get_conection(self):
        connect = psycopg.connect(f" dbname = {self.dbname} user = {self.user} password = {self.password}")
        return connect



class Profile:
    # ''' Данный класс содержит конструктор и метод set_profile и get_profile для добавления и получения
    #  пользователя соответсвенно'''

    # В констукторе инициализируем атрибуты сущности Profile
    # conn = None
    def __init__(self, id_user, surname, name, patronymic, age, dt_create, status):
        self.id_user = id_user
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.age = age
        self.dt_create = dt_create
        self.status = status

    # def set_conn(self,conn):
    # подключение к БД через функцию
    #     self.conn = conn.cursor()

    # в аргументе conn передается дискриптор подключения к БД
    def set_profile(self, conn):
        # Добавляет профиль в БД
        # self.conn.execute () если через фунцию (тогда аргумент conn убираем)
        cur = conn.cursor()
        cur.execute(f"""
                        INSERT INTO users (id_user, surname, name, patronymic, age, dt_create, status)
                        VALUES  ({self.id_user}, '{self.surname}', '{self.name}', '{self.patronymic}',{self.age},
                         '{self.dt_create}', {self.status});
                        """)
        conn.commit()



    def get_profile(self, conn):
        # Извлекает профиль из БД
        cur = conn.cursor()
        cur.execute(f"""SELECT * FROM users where surname ='{self.surname}';""")
        obj  = cur.fetchall()
        conn.commit()
        return obj




connection = DB(dbname = "testsystem", user = "testsystem", password = "12345")
conn = connection.get_conection()
new_user = Profile(10 , 'Зигмунд', 'Фрейд','Фрейдович',50,'2020-10-10 15:45:00', True)
new_user.set_profile(conn)
print(new_user.get_profile(conn))
conn.close()






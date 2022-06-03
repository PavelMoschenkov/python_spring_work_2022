# Сделать рефакторинг кода задачи 35.
#  1. Реализовать из класса DB синглтон. Экземляр класса должен быть единственным.
#  2. Сделать класс View абстрактным, а также метод render() абстрактным
#  3. Реализовать  фабрику FabConsoleView в которой пораждаются экзепляры
#     классов TestView, QuestionView и AuthView

import psycopg
from abc import ABC, abstractmethod

class DB:
    '''Данный класс содержит конструктор и метод get_connect. В конструкторе инициализируются переменные
        (атрибуты доступа к БД) . Метод возвращает соединение.'''
    __instance__ = None
    def __init__(self, dbname, user, password):
        # Проверяем конструктор на сущ. экземпляр
        self.dbname = dbname
        self.user = user
        self.password = password
        if DB.__instance__ is None:
            DB.__instance__ = self
        else:
            raise Exception("We can not creat another class")

    @staticmethod
    def get_instans(): #определяем статический метод для получения экземпляра
        if not DB.__instance__:
            DB()
        return DB.__instance__

    def get_conection(self):
        self.connect = psycopg.connect(f" dbname = {self.dbname} user = {self.user} password = {self.password}")
        return self.connect



class View(ABC):
    """ 'Абстрактный' класс для потомков """
    @abstractmethod
    def render(self):
        raise NotImplementedError('This method should have implemented.')
    print('Абстрактный класс для потомков')


class TestView(View):
    """В классе перегружаем виртуальный метод  render от родителя"""
    def render(self):
        print('virtual', type(TestView))

        """Метод реализует отрисовку экранной формы выбора билета """

class QuestionView(View):
    """В классе перегружаем виртуальный метод  render от родителя"""

    def render(self):
        """Метод реализует отрисовку вопроса с вариантами ответа и строкой выбора варианта"""
        print('virtual', type(QuestionView))



class RegistrationView(View):
     # """В классе перегружаем виртуальный метод  render от родителя"""
    def render(self):
        # """Метод реализует отрисовку регистрации пользователя"""
        print('virtual',type(RegistrationView))


class ViewFactory:
    def getView(self, ViewType):
        if ViewType == 'QuestionView':
            return QuestionView()
        elif ViewType == 'TestView':
            return TestView
        elif ViewType == 'RegistrationView':
            return RegistrationView()
        else:
            pass


connection = DB(dbname = "testsystem2", user = "pavel", password = "12345;")
connection.get_conection()
print(connection)
# создаем второе подключение оно должно не работать
# obj = DB(dbname = "testsystem2", user = "pavel", password = "12345;")
# obj.get_conection()
# print(obj)
obj = ViewFactory()
m = obj.getView("TestView")
m.render(self=True)
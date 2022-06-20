# Реализовать две сопрограммы. Первая с заданной периодичность(раз в 2,3 сек) пишет в файл и выводит результат.
# другая делает запрос к БД на выборку  билета и отображает поочередно  название билета (раз в 2,3 сек)

import asyncio
import asyncpg
import datetime
from aiofile import async_open

async def logger():
    print(f"открывыю файл {datetime.datetime.now()}")
    async with async_open("text.txt", "a+", encoding="utf-8") as fd:
        print(f"1 запись в файл {datetime.datetime.now()}")
        await fd.write('Hello\n')
        await asyncio.sleep(2)
        print(f"2 запись в файл {datetime.datetime.now()}")
        await fd.write('World\n')
        # await fd.close()
        # print(f"file closed {datetime.datetime.now()}")


class Test:
    """ В классе реализуем методы работы с БД """
    @classmethod
    async def get_list_tests(cls):
        """В методе  получаем список тем """
        # Метод возвращает соединение к БД
        print(f"соединение с БД {datetime.datetime.now()}")
        conn = await asyncpg.connect(host="localhost", port=5432, user="pavel", database="testsystem2",
                                      password="12345;")
        print(f"CONNECT ON, IN LOAD... {datetime.datetime.now()}")
        cur = await conn.fetchval(f"""SELECT "Theme" FROM test;""")
        print(f"theme:{cur} {datetime.datetime.now()}")


async def main():
    await asyncio.gather(logger(), Test.get_list_tests())

asyncio.run(main())


# Bonus:
# В качестве бонуса можно реализовать Telegtram - бота который в виде викторины задает
# вопросы. Вопросы можно взять из тестовой системы. После вывода бот принимает вариант ответа.
# В конце викторины выводит кол-во правильных и неправильных ответов и приз в случае успеха.
# В качестве библиотеки можно взять  библиотеку telebot. Описание по разработки и примеры найти
# в многочисленных статьях в Internet.




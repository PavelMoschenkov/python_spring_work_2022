# Шифр Цезаря
# Описание шифра.
# В криптографии шифр Цезаря, также известный шифр сдвига, код Цезаря или сдвиг Цезаря,
# является одним из самых простых и широко известных методов шифрования.
# Это тип подстановочного шифра, в котором каждая буква в открытом тексте заменяется буквой на некоторое
# фиксированное количество позиций вниз по алфавиту. Например, со сдвигом влево 3, D будет заменен на A,
# E станет Б, и так далее. Метод назван в честь Юлия Цезаря, который использовал его в своей частной переписке.
#
# Задача.
# Считайте файл message.txt и зашифруйте  текст шифром Цезаря, при этом символы первой строки файла должны
# циклически сдвигаться влево на 1, второй строки — на 2, третьей строки — на три и т.д.
#  В этой задаче удобно считывать файл построчно, шифруя каждую строку в отдельности.
# В каждой строчке содержатся различные символы. Шифровать нужно только буквы кириллицы.



import codecs




def encrypt_caesar_ru(ciphertext: str, shift: int = 3) -> str:
    i = 0
    up = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    down = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    plaintext = [ciphertext[j] for j in range(len(ciphertext))] # через строку-алфавит, несколько раз его копируем и делаем шифт с "подушкой безопасности" в виде первых 30 букв
    for letter in ciphertext:
        if letter.isalpha() and letter.isupper() and letter not in 'QWERTYUIOPASDFGHJKLZXCVBNM': #по заглавным, ДОБАВИЛ АНГЛ АЛФАВИТ, ЧТОБЫ ЦИФРЫ НЕ СЧИТЫВАЛИСЬ ЗА БУКВЫ И ВЫДАВАЛИ ОШИБКУ
            plaintext[i] = up[up.index(letter, 33) - shift-1]
        elif letter.isalpha() and letter.islower() and letter not in 'QWERTYUIOPASDFGHJKLZXCVBNM': #по строчным
            plaintext[i] = down[down.index(letter, 33) - shift-1]
        else:
            plaintext[i] = letter #не буквы просто добавляем
        i += 1
    return ''.join(plaintext)

print(encrypt_caesar_ru('У А ЕЕЕ', 3)) #просто тесты, ТОЛЬКО РУ БУКВЫ

f = codecs.open( "message.txt", "r", "utf-8" )#открываем файл
num = 1 #первоначальный сдвиг
while True:
    line = f.readline()
    if len(line) == 0: #читаем пока читается (пока ридлайн не выдаст пустую строку)
        break
    print(encrypt_caesar_ru(line, num)) #выводим ответ для данной строки
    num += 1 #увеличиваем сдвиг на 1, как в задании.
f.close()



# Для написанной игры "Поле чудес" нужно сделать рефакторинг кода , сгруппировать
# функционал в логические блоки и оформить эти блоки кода в виде функций. Стараться
# чтобы каждая функция выполняла одно универсальное действие.


import random as rd


word_index = [0, 1, 2]
word_index = rd.sample(word_index, 3)
print("""Добро пожаловать в игру: Поле чудес!""")
questions = ['Спортивная машина с конем на значке?', 'На чем летают люди на длительные растояния?', 'Что пьют по утрам в Лондоне?']
answers = ['ФЕРРАРИ', 'САМОЛЕТ', 'ЧАЙ']

def add_letter(word, letter, answer):
    ind1 = -1
    for num_letter in range(curr_answer.count(letter)):
        ind1 = answer.index(letter, ind1 + 1)
        word[ind1] = letter
    return word

def add_error(errors):
    errors += 1
    return errors


def check_letter(cur_word, answer, letter):
    if (letter in answer) and (letter not in cur_word):
        add_letter(word, letter, curr_answer)
        return True
    elif letter in word:
        print("Вы уже использовали эту букву")
        return False
    else:
        return False

def is_win(word, answer):
    if word == answer:
        return True
    else:
        return False

for attempt in word_index:
    curr_answer = list(answers[attempt])
    print(f"Ваш вопрос: {''.join(questions[attempt])}")
    errors = 0
    word = list('▒' * len(answers[attempt]))
    while errors < 10:
        if is_win(word, curr_answer):
            print(f"Поздравляем, вы отгадали слово! Ответ {word}")
            break
        print(f"Отгадано на данный момент: {''.join(word)}")
        letter = input('Введите букву')
        if check_letter(word, curr_answer, letter):
            word = add_letter(word, letter, curr_answer)
        else:
            print(f"Вы ошиблись! У вас осталось {10 - errors} попыток")
            errors = add_error(errors)
print("Игра закончена")
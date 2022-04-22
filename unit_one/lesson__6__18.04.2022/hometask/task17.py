# Создайте функцию compute_bill, считающаю итоговую сумму товаров в чеке.
# Функция должна принимать 1 параметр - словарь, в котором указано количество едениц товара.
# Цены хранятся в словаре:


# 1-й вариант

print("Добрый день сумма Вашей покупки составляет:")

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
def compute_bill(chek):
    total = 0
    for key, val in chek.items():
        x = input(f'Введите количество {key}: ')
        total += val * int(x)
    return total


print(compute_bill(prices), "руб.")

# 2-й вариант

# print("Добрый день вы в магазине, можете выбрать из списка количество товара и мы посчитаем стоимость вашей корзины!")
# total = 0
# for key, val in prices.items():
#     x = input(f'Введите количество {key}: ')
#     total += val * int(x)
# print(total,"руб.")



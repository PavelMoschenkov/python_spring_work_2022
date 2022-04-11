# задача 4
a = int(input('Введите сторону квадрата (a): '))
S = a * a
print('Площадь квадрата S: ', S)
print(type(a))

# задача 5

a = float(input('введите число (a)'))
b = float(input('введите число (b)'))
c = float(input('введите число (с)'))

ac = abs(c - a)
print('AC -', ac)
bc = abs(c - b)
print('BC -', bc)
print('Сумма -', ac + bc)

# задача 6 не понял как

a = int(input("введите значение (a)="))
b = int(input("введите значение (b)="))
if a != 0:
    print('x =', -b/a)
else:
    print('а = 0')


# задача 7
a = int(input('введите число'))
if a % 2 == 0:
    print('четное число')
else:
    print('нечетное число')

# задача №8
a, b, c = input().split()
a, b, c = c, a, b
print(a, b, c)

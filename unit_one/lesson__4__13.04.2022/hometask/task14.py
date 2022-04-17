#  Дан массив размера N. Найти индексы двух ближайших чисел из этого массива.

# Пример:
# mass = [1,2,17,16,30,51,2,70,3,2]

# Для числа 2 индексы двух ближайших чисел: 6 и 9

# Пример:
# mass = [1,2,17,54,30,89,2,1,6,2]
# Для числа 1 индексы двух ближайших чисел: 0 и 7
# Для числа 2 индексы двух ближайших чисел: 6 и 9
#  найти пару одинаковых чисел, найти индексное растояние (наименьший путь от точки а в точку б)
#


mass = [1,2,17,54,30,89,2,1,6,2]
nums = []
for i in range(len(mass)):
    mass_ind = []
    num = mass[i]
    cnt = mass.count(num)
    if cnt > 1 and num not in nums:
        nums.append(num)

for number in nums:
    mass_ind = []
    ind_1 = mass.index(number)
    mass_ind.append(ind_1)
    for j in range(mass.count(number) - 1):
        ind_1 = mass.index(number, ind_1+1)
        mass_ind.append(ind_1)

    itog_razn = -1000000
    itog_index = []
    for h in range(len(mass_ind) - 1):
        if mass_ind[h] - mass_ind[h+1] > itog_razn:
            itog_razn = mass_ind[h] - mass_ind[h+1]
            itog_index = [mass_ind[h], mass_ind[h+1]]

    print('Для числа ', number , 'индексы двух ближайших чисел', itog_index)

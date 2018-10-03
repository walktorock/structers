# coding : utf-8

#2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

a = input('Введите натуральное число:')

chet = []
nechet = []
for i in a:
    if int(i) % 2 != 0:
        nechet.append(i)
    elif int(i) == 0:
        continue
    else:
        chet.append(i)

print(f'Четных {len(chet)}')
print(f'Нечетных {len(nechet)}')

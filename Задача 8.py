# coding : utf-8

# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

nums = []
ans = int(input('Введите количество чисел, которые хотите ввести: '))
mainnum = input('Введите цифру, которую хотите посчитать: ')
mnlist = []
i = 1
while i < ans + 1:
    chislo = input(f'Введите число {i}: ')
    nums.append(f'{chislo}')
    i += 1

for n in str(nums):
    if n == mainnum:
        mnlist.append(n)


print(f'Указанное число встречается {len(mnlist)} раз/а')
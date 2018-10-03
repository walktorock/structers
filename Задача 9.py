# coding : utf-8

# 9. Среди натуральных чисел, которые были введены,
# найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

nums = []
ans = int(input('Введите количество чисел, которые хотите ввести: '))
mainnum = input('Введите цифру, которую хотите посчитать: ')
mnlist = []
mark = []
i = 1
while i < ans + 1:
    chislo = input(f'Введите число {i}: ')
# здесь пробую добавлять в новый список сумму цифр числа, получается как то не очень
    for c in chislo:
        mark.append(int(c % 10) + int(c // 10))
    if int(chislo) == 0:
       print(f'Наибольшая сумма цифр {max(mark)}')
       break
    nums.append(chislo)
    i += 1

for n in str(nums):
    if n == mainnum:
        mnlist.append(n)


print(f'Указанное число встречается {len(mnlist)} раз/а')

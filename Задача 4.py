# coding : utf-8

import random

#случайное число
a = int(input('Введите начало диапазона'))
b = int(input('Введите конец диапазона'))
print(random.randint(a, b))

# случайный символ
a = input('Введите начало диапазона')
b = input('Введите конец диапазона')
n1 = ord(a)
n2 = ord(b)
print(chr(random.randint(n1, n2)))

#Так и не разобрался, что такое вещественные числа

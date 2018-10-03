# codinf : utf-8
import random
#2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй
# массив надо заполнить значениями 0, 3, 4, 5 (индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

array = [random.randint(1, 100) for _ in range(10)]
print(array)
index_array = []

for index, value in enumerate(array):
    if value % 2 == 0:
        index_array.append(index)

print(f'Четные числа под индексами: {index_array}')
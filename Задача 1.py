# coding : utf-8

import random

# 1. Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Вывести на экран исходный и отсортированный массивы.

random_list = [i for i in range(-100, 100 )]
random.shuffle(random_list)

print(f'Перемешанный список: \n{random_list}\n')
def bub_sort(random_list):
    n = 1

    while n < len(random_list):

        for i in range(len(random_list) - n):
            if random_list[i] < random_list[i + 1]:
                random_list[i], random_list[i + 1] = random_list[i + 1], random_list[i]

        n +=1
    print(f'Отсортированный список: \n{random_list}')
bub_sort(random_list)
# coding : utf-8

import random

# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

fl_list = []
n = 0
while n < 10:
    fl_list.append(random.random() * 49)
    n +=1
print(fl_list)
def merge_sort(a):
    if len(a) <= 1:
        return a
    middle = int(len(a)) / 2
    left = merge_sort(a[:middle])
    right = merge_sort(a[middle:])
    return merge(left, right)

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if len[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    if len(left) > 0:
        result += left
    if len(right) > 0:
        result += right
    return result

merge_sort(fl_list)
print(fl_list)
# coding : utf-8
import sys
#1. Подсчитать, сколько было выделено памяти под переменные в ранее
# разработанных программах в рамках первых трех уроков. Проанализировать
# результат и определить программы с наиболее эффективным использованием памяти.
# Для анализа возьмите любые 1-3 ваших программы. Результаты анализа
# вставьте в виде комментариев к коду.
# P.S. Напишите в комментариях версию Python и разрядность ОС.

#def count(num):
num = '15298584518873885698355'
chet = []
nechet = []
for i in num:
    if int(i) % 2 != 0:
        nechet.append(i)
    elif int(i) == 0:
        continue
    else:
        chet.append(i)


    #print(f'Четных {len(chet)}')
    #print(f'Нечетных {len(nechet)}')


def show_size(x, level=0):
    print('\t' * level, f'type = {x.__class__}, size = {sys.getsizeof(x)}, object = {x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for y in x.items():
                show_size(y, level + 1)
        elif not isinstance(x, str):
            for y in x:
                show_size(y, level + 1)
#show_size(num)
# type = <class 'str'>, size = 48, object = 15298584518873885698355

#show_size(chet)
#    type = <class 'list'>, size = 100, object = ['2', '8', '8', '4', '8', '8', '8', '8', '6', '8']
# 	 type = <class 'str'>, size = 26, object = 2
# 	 type = <class 'str'>, size = 26, object = 8
# 	 type = <class 'str'>, size = 26, object = 8
# 	 type = <class 'str'>, size = 26, object = 4
# 	 type = <class 'str'>, size = 26, object = 8
# 	 type = <class 'str'>, size = 26, object = 8
# 	 type = <class 'str'>, size = 26, object = 8
# 	 type = <class 'str'>, size = 26, object = 8
# 	 type = <class 'str'>, size = 26, object = 6
# 	 type = <class 'str'>, size = 26, object = 8

#show_size(nechet)
#    type = <class 'list'>, size = 100, object = ['1', '5', '9', '5', '5', '1', '7', '3', '5', '9', '3', '5', '5']
# 	 type = <class 'str'>, size = 26, object = 1
# 	 type = <class 'str'>, size = 26, object = 5
# 	 type = <class 'str'>, size = 26, object = 9
# 	 type = <class 'str'>, size = 26, object = 5
# 	 type = <class 'str'>, size = 26, object = 5
# 	 type = <class 'str'>, size = 26, object = 1
# 	 type = <class 'str'>, size = 26, object = 7
# 	 type = <class 'str'>, size = 26, object = 3
# 	 type = <class 'str'>, size = 26, object = 5
# 	 type = <class 'str'>, size = 26, object = 9
# 	 type = <class 'str'>, size = 26, object = 3
# 	 type = <class 'str'>, size = 26, object = 5
# 	 type = <class 'str'>, size = 26, object = 5

# Версия Python 3.7.0, разрдность системы: 64
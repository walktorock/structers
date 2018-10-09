# coding : utf-8
import cProfile

#2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

def count(num):

    chet = []
    nechet = []
    for i in num:
        if int(i) % 2 != 0:
            nechet.append(i)
        elif int(i) == 0:
            continue
        else:
            chet.append(i)

    print(f'Четных {len(chet)}')
    print(f'Нечетных {len(nechet)}')
#почему то не смог выполнить timeit через терминал, встроенный в пайчар, директория не хотела меняться, пришлось
#использовать командную строку
#100 loops, best of 5: 543 usec per loop
#100 loops, best of 5: 565 usec per loop

#cProfile.run('count("1234567")')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_1.py:7(count)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#         7    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

#4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125, ...
# Количество элементов (n) вводится с клавиатуры.


def chain(n):
    list = []
    i = 0
    z = 1
    while i < n:
        list.append(z)
        z = (z * (-0.5))
        i += 1
    print(list)
    b = sum(list)
    print(b)

#100 loops, best of 5: 6.98 msec per loop
#100 loops, best of 5: 6.97 msec per loop
#cProfile.run('chain(1000)')

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.005    0.005 <string>:1(<module>)
#         1    0.000    0.000    0.005    0.005 task_1.py:40(chain)
#         1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
#         2    0.005    0.003    0.005    0.003 {built-in method builtins.print}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
#      1000    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
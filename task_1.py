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

cProfile.run('count("1234567")')
#      ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_1.py:7(count)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#         7    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


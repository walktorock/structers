# coding : utf-8
import cProfile
#решето
def si(n):
    sieve = [i for i in range(n)]
    sieve[1] = 0
    for i in range(2, n):
        if sieve[i] != 0:
            j = i * 2
            while j < n:
                sieve[j] = 0
                j += i
    sieve = [i for i in sieve if i != 0]
    print(sieve)

# 100 loops, best of 5: 87.1 usec per loop
# 100 loops, best of 5: 80.3 usec per loop
# 100 loops, best of 5: 93.3 usec per loop

# cProfile.run('si(1000)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        # 1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        # 1    0.000    0.000    0.000    0.000 task_2.py:13(<listcomp>)
        # 1    0.000    0.000    0.001    0.001 task_2.py:4(si)
        # 1    0.000    0.000    0.000    0.000 task_2.py:5(<listcomp>)
        # 1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        # 1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        # 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Опять таки проблема со временем, не хватает на второй алгоритм без решета
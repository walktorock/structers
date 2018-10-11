# coding : utf-8

from  collections import namedtuple

#1. Пользователь вводит данные о количестве предприятий,
#  их наименования и прибыль за 4 квартала для каждого предприятия.
#  Программа должна определить среднюю прибыль
#  (за год для всех предприятий) и вывести наименования предприятий,
#  чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.


kol = int(input('Введите количество предприятий: '))
orgs = []
names = []
New_Org = namedtuple('New_Org', 'name in_1q in_2q in_3q in_4q avg')
for i in range(1, kol + 1):
    name = input(f'Введите название организации {i}: ')
    names.append(name)
    in_1q = int(input('Введите прибыль за 1 квартал: '))
    in_2q = int(input('Введите прибыль за 2 квартал: '))
    in_3q = int(input('Введите прибыль за 3 квартал: '))
    in_4q = int(input('Введите прибыль за 4 квартал: '))
    avg = (in_1q + in_2q + in_3q + in_4q) / 4
    org_1 = New_Org(name,in_1q, in_2q, in_3q, in_4q, avg)
    orgs.append(org_1)
n = 0
total = 0
while n < kol:
    total += orgs[n].avg
    n += 1
total_avg = total / kol

print(f'Средняя прибыль для организаций {names} за год составила {total_avg}')
m = 0
while m < kol:
    if orgs[m].avg > total_avg:
        print(f'Прибыль организации {orgs[m].name} выше среднего')
    elif orgs[m].avg <= total_avg:
        print(f'Прибыль организации {orgs[m].name} ниже среднего')
    m +=1
# coding : utf-8

from  collections import Counter, defaultdict, namedtuple

#1. Пользователь вводит данные о количестве предприятий,
#  их наименования и прибыль за 4 квартала для каждого предприятия.
#  Программа должна определить среднюю прибыль
#  (за год для всех предприятий) и вывести наименования предприятий,
#  чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

# kol = int(input('Введите количество предприятий: '))
# orgs = []
# incomes = []
# for i in range(1, kol + 1):
#     orgs.append(input(f'Введите название организации {i}: '))
#     incomes.append(int(input(f'Введите прибыль организации {orgs[i - 1]} за 4 квартала: ')))
# print(orgs)
# print(incomes)
kol = int(input('Введите количество предприятий: '))
orgs = []
New_Org = namedtuple('New_Org', 'name in_1q in_2q in_3q in_4q')
for i in range(1, kol + 1):
    name = input('Название')
    in_1q = int(input('Введите прибыль за 1 квартал: '))
    in_2q = int(input('Введите прибыль за 2 квартал: '))
    in_3q = int(input('Введите прибыль за 3 квартал: '))
    in_4q = int(input('Введите прибыль за 4 квартал: '))
    org_1 = New_Org(name,in_1q, in_2q, in_3q, in_4q)
    orgs.append(org_1)
n = 0
while n < kol :
    avg = (orgs[n].in_1q + orgs[n].in_2q + orgs[n].in_3q + orgs[n].in_4q) / 4
    print(f'Средняя прибыли организации {orgs[n].name} = {avg} ')
    n += 1

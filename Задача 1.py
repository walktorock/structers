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
New_Org = namedtuple('New_Org', 'name income_1q income_2q income_3q income_4q')
for i in range(1, kol + 1):
    name = input('Название')
    income_1q = input('Введите прибыль за 1 квартал')
    income_2q = input('Введите прибыль за 2 квартал')
    income_3q = input('Введите прибыль за 3 квартал')
    income_4q = input('Введите прибыль за 4 квартал')
    org_1 = New_Org(name,income_1q, income_2q, income_3q, income_4q)
    orgs.append(org_1)

print(orgs)
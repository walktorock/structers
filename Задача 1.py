# codinf : utf-8

#1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.

# nums = [i for i in range(2, 100)]
# # deliteli = [2, 3, 4, 5, 6, 7, 8, 9]
# #
# # krat2 = 0
# # krat3 = 0
# # krat4 = 0
# # krat5 = 0
# # krat6 = 0
# # krat7 = 0
# # krat8 = 0
# # krat9 = 0
# # # знаю, что скорее всего есть более красивое решение, но на дз очень мало времени
# # for num in nums:
# #     if num % 2  == 0:
# #         krat2 += 1
# #     if num % 3 == 0:
# #         krat3 += 1
# #     if num % 4 == 0:
# #         krat4 += 1
# #     if num % 5 == 0:
# #         krat5 += 1
# #     if num % 6 == 0:
# #         krat6 += 1
# #     if num % 7 == 0:
# #         krat7 += 1
# #     if num % 8 == 0:
# #         krat8 += 1
# #     if num % 9 == 0:
# #         krat9 += 1
# #
# #
# # print(f'Кратных 2: {krat2},\n Кратных 3: {krat3},\n Кратных 4: {krat4},\n Кратных 5: {krat5},\n '
# #       f'Кратных 6: {krat6},\n Кратных 7: {krat7},\n Кратных 8: {krat8},\n Кратных 9: {krat9}\n')

a = [0] * 8
for i in range(2, 100):
    for j in range(2, 10):
        if i % j == 0:
            a[j - 2] += 1
for idx, i in enumerate(a, start=2):
    print(f'Числу {idx} кратно {i}')
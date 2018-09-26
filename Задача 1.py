# coding : utf-8

n = int(input('Введите техзначное число: '))
a = (n//100)
b = (n//10%10)
c = (n%10)

print(a*b*c)
print(a+b+c)
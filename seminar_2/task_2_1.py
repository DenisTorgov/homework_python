# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#     Пример:
# - 6782 -> 23
# - 0,56 -> 11

import math

x = float(input('Введите вещественное число точностью не более двух знаков после запятой : '))
sum = 0

subzero = x % 1
x = x - subzero
if subzero > 0:
    print('ok')
    while subzero != 0:
        subzero = round(subzero * 10, 2)
        print(subzero)
        sum += subzero // 1
        print(sum)
        subzero = subzero % 1

while x > 0:
    sum += x % 10
    x = x // 10

print(f'Сумма равна {sum:.0f}')
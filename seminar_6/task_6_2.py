# Задайте список из нескольких чисел. Напишите программу, которая
# найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

x = int(input("Введите количество элементов списка: "))

if x == 0 or x < 0:
    print('Число должно быть больше нуля')
else:
    randomlist = [random.randint(0, 10) for i in range(x)]
    # for i in range(x):
    #     randomlist[i] = random.randint(0, 10)

i = 1
multi = 1

while i < len(randomlist):
    multi *= randomlist[i]
    i +=2
print(randomlist)
print(multi)
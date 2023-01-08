# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний
# и т.д.
#     Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

x = int(input("Введите количество элементов списка: "))

if x == 0 or x < 0:
    print('Число должно быть больше нуля')
else:
    randomlist = [0]*x
    for i in range(x):
        randomlist[i] = random.randint(0, 10)

print(randomlist)

halflength = x // 2
newlist = [0]*halflength
i = 0

while i < halflength:
    newlist[i] = randomlist[i] * randomlist[len(randomlist) - i - 1]
    i += 1

if x % 2 != 0:
    newlist.append(randomlist[halflength]**2)

print(newlist)
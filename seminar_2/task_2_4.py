# Задайте список из N элементов, заполненных числами из промежутка
# [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции хранятся в отдельном списке
# ( пример n=4, lst1=[4,-2,1,3] - списко на основе n,
# а позиции элементов lst2=[3,1].

import random

x = int(input("Введите количество элементов: "))

if x == 0 or x < 0:
    print('Число должно быть больше нуля')
else:
    randomlist = [0]*x
    for i in range(x - 1):
        randomlist[i] = random.randint(-x, x)

print(randomlist)
positions = [0, 2]
multi = 1

for i in range(2):
    multi *= randomlist[int(positions[i])]
    
print(f'Произведение эелементов на превой и третьей позиции равно {multi}')
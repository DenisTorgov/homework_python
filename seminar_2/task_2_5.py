# Реализуйте алгоритм перемешивания списка. (рандомно поменять
# местами элементы списка между собой)

import random

x = int(input("Введите количество элементов: "))

if x == 0 or x < 0:
    print('Число должно быть больше нуля')
else:
    randomlist = [0]*x
    for i in range(x - 1):
        randomlist[i] = random.randint(0, 100)

print(randomlist)

for i in randomlist:
    r1 = random.randint(0, x-1)
    r2 = random.randint(0, x-1)
    temp = randomlist[r1]
    randomlist[r1] = randomlist[r2]
    randomlist[r2] = temp
 
print(randomlist)
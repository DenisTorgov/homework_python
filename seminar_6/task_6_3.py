# Задайте число. Составьте список чисел Фибоначчи, в том числе для
# отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def Phibonachi (a):
    if a == 0: return 0
    if a == 1: return 1
    return Phibonachi(a - 1) + Phibonachi(a - 2) 

x = int(input("Введите количество чисел последовательности Фибоначчи: "))

positivelist = [i for i in range(x + 1)]

positivelist = list(map(Phibonachi, positivelist))

# for i in range(x + 1):
#     positivelist.append(Phibonachi(i))

negativelist = [i * -1 for i in positivelist]
del negativelist[1]
negativelist.reverse()
negativelist.extend(positivelist)
print(negativelist)
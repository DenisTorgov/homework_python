# Напишите программу, которая принимает на вход число N и выдает
# набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def factorial (a):
    if a == 0: return 1
    if a == 1: return 1
    return a * factorial(a - 1)


x = int(input("Введите целое положительное число для вычисления факториала: "))

if x == 0 or x < 0:
    print('Число должно быть больше нуля')
else:
    for i in range(x - 1):
        print(f'{factorial(i+1)}, ', end='')
    print(f'{factorial(x)}')
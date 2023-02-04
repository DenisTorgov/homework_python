# noughts and crosses

import random

field = [[1, 2, 3], [4, 5, 6] , [7, 8, 9]]
winfield = [[['z', 2, 3], ['z', 5, 6] , ['z', 8, 9]],
[[1, 'z', 3], [4, 'z', 6] , [7, 'z', 9]],
[[1, 2, 'z'], [4, 5, 'z'] , [7, 8, 'z']],
[['z', 'z', 'z'], [4, 5, 6] , [7, 8, 9]],
[[1, 2, 3], ['z', 'z', 'z'] , [7, 8, 9]],
[[1, 2, 3], [4, 5, 6] , ['z', 'z', 'z']],
[['z', 2, 3], [4, 'z', 6] , [7, 8, 'z']],
[[1, 2, 'z'], [4, 'z', 6] , ['z', 8, 9]]]


def printfield (field):

    print(' _____________ \n')
    for i in range(3):
        for j in range(3):
            print(' | ' + str(field[i] [j]), end ='')
        print(' | \n _____________ \n')

def playermove(f):
    x = int(input('->'))
    if x < 1 or x > 9 or not str(x).isdigit():
        print('Нужно ввести число от 1 до 9. Попробуйте еще раз')
        return playermove(f)
    i =-1
    j =-1
    i = (x -1)// 3
    if x % 3 == 0:
        j = 2
    else:
        j = x % 3 - 1
    if str(f[i] [j]).isdigit():
        f[i] [j] = 'O'
        return f
    else:
        print('Это поле уже занято введите другое')
        return playermove(f)

def cpumove(f):
    i=-1
    j=-1
    i = random.randint(0, 2)
    j = random.randint(0, 2)
    if str(f[i] [j]).isdigit():
        f[i] [j] = 'X'
        return f
    else:
        return cpumove(f)

def wincheck(f, mark):
    for m in range(8):
        count = 0
        for n in range(3):
            for k in range(3):
                if str(f [n] [k]) ==  mark and not str(winfield [m] [n] [k]).isdigit():
                    count += 1
                    if count == 3: return 1
    return 0

print('Начало игры в крестики-нолики. Выберите номер поля для хода')
printfield(field)

winner = 0
move = 0

while move < 9:
    field = playermove(field)
    winner = wincheck(field, 'O')
    printfield(field)
    if winner:
        print('Поздравляем вы победили!')
        break
    move +=1
    if move == 9:
        print('Ничья')
        break
    field = cpumove(field)
    winner = wincheck(field, 'X')
    printfield(field)
    if winner:
        print('Компьютер оказался умней. Слава роботам!')
        break
    move +=1

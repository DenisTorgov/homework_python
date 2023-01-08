# Напишите программу, которая будет преобразовывать десятичное число
# в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

x = int(input("Введите целое число для преобразования в двоичную систему: "))

binarlist = []

while x > 0:
    if round(x % 2, 1) == 0:
        binarlist.append("0")
    else: 
        binarlist.append("1")
    x = x // 2
    
binarlist.reverse()
print("".join(binarlist))



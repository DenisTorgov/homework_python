# Задайте список из n чисел последовательности (1+1/n)**n и выведите
# на экран их сумму.

def element (a):
    return (1+1/a)**a

x = int(input("Введите целое положительное число для вычисления последовательности: "))

sequence = [0]*x
sum = 0
for i in range(x):
    sequence[i] = float(element(i+1))
    sum += sequence[i]

print(sequence)
print(f'Сумма последовательности равна {sum:.5f}')
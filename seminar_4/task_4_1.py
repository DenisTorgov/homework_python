

def factorial (a):
    if a == 0: return 1
    return a * factorial(a - 1)

precision = float(input("Введите точность вычисления числа e: "))

n = 0
e0 = 1 / factorial(n)
e = e0 + 1 / factorial(n + 1)

print(e, e0)

while e - e0 > precision:
    n += 1
    e0 += 1 / factorial(n)
    e += 1 / factorial(n + 1)
    
num = precision
i = 0
while num < 0:
    num *= 10
    i += 1

print(f"Число e с точностью {precision}, равно {e}. \nСуммировано {n+1} членов ряда")
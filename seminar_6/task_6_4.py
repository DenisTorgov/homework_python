

import random
def sortm ():
    if randomfactor == 0:
        continue
    elif randomfactor == 1:
        file.write(f"x^{k} + ")
    elif k > 1:
        file.write(f"{randomfactor}x^{k} + ")
    elif k == 1:
        file.write(f"{randomfactor}x + ")
    else:
        file.write(f"{randomfactor} = 0")

degree  = int(input("Задайте степень многочлена: "))

file = open("seminar_6\\task_6_4.txt", "w")

randomfactor = [random.randint(0, 100) for i in range(degree, -1, -1)]
result = list(zip(range(degree, -1, -1), randomfactor))
file.write(str(result))


# for k in range(degree, -1, -1):
#     randomfactor = random.randint(0, 100)
#     if randomfactor == 0:
#         continue
#     elif randomfactor == 1:
#         file.write(f"x^{k} + ")
#     elif k > 1:
#         file.write(f"{randomfactor}x^{k} + ")
#     elif k == 1:
#         file.write(f"{randomfactor}x + ")
#     else:
#         file.write(f"{randomfactor} = 0")



file.close()

with open("seminar_6\\task_6_4.txt", "r") as file1:
    for line in file1:
        print(line)


import random
def sortm (i):
    if i[1] == 0:
        return ""
    elif i[1] == 1:
        return f"x^{i[0]} + "
    elif i[0] > 1:
        return f"{i[1]}x^{i[0]} + "
    elif i[0] == 1:
        return f"{i[1]}x + "
    else:
        return f"{i[1]} = 0"

degree  = int(input("Задайте степень многочлена: "))

file = open("seminar_6\\task_6_4.txt", "w")

randomfactor = [random.randint(0, 100) for i in range(degree, -1, -1)]
result = list(zip(range(degree, -1, -1), randomfactor))
result = list(map(sortm, result))
print(len(result))
result = str(''.join(result))
file.write(result)

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
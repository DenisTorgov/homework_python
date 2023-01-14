


def todictionary(line):
    d ={}
    max_k = 0
    for i in range(len(line)):
        line[i] = line[i].strip()
        position_x = line[i].find("x^")
        if position_x > 0:
            d[line[i] [position_x +2:]] = line[i] [0: position_x]
        elif line[i] [-1] == "x" :
            d[0] = line[-2] [0: -1]
        if position_x > 0:
            if max_k < int(line[i] [position_x + 2:]):
                max_k = int(line[i] [position_x + 2:])
                d["max_k"] = max_k
    d[-1] = line[-1] [:-4]
    return d

file1 = open("seminar_4\\task_4_5_1.txt", "r")
file2 = open("seminar_4\\task_4_5_2.txt", "r")
d1 = todictionary(file1.readline().split("+"))
d2 = todictionary(file2.readline().split("+"))

if d1["max_k"] < d2["max_k"]:
    max = d2["max_k"]
else:
    max = d1["max_k"]

result = ""
for i in range(max, 1, -1):
    print(i)
    print(d1.setdefault(f"{i}", 0), d2.setdefault(f"{i}", 0))
    if str(d1.setdefault(f"{i}", 0)) == "0" and str(d2.setdefault(f"{i}", 0)) == "0":
        continue
    elif str(d1.setdefault(f"{i}", 0)) == "0":
        result += str(int(str(d2.setdefault(f"{i}"))))
        result +=f"x^{i} + "
    elif str(d2.setdefault(f"{i}", 0)) == "0":
        result += str(int(str(d1.setdefault(f"{i}"))))
        result +=f"x^{i} + "
    else:
        result += str(int(str(d1.setdefault(f"{i}", "0"))) + int(str(d2.setdefault(f"{i}", "0"))))
        result +=f"x^{i} + "
result += str(int(str(d1[0])) + int(str(d2[0])))
result += "x + "
result += str(int(str(d1[-1])) + int(str(d2[-1])))
result +=" = 0"

print("Результат сложения многочленов из файлов task_4_5_1.txt и  task_4_5_2.txt")
print(f"{result}")

file = open("seminar_4\\task_4_5.txt", "w")
file.write(result)
file.close()

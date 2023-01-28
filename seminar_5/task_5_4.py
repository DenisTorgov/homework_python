# Реализуйте RLE алгоритм: реализуйте модуль сжатия
# и восстановления данных.

file = open("seminar_5\\task_5_4_input.txt", "r")
stringA = file.readline()
print(stringA)
result = ""
count = 1

for i in range(len(stringA) - 1):
    letter = stringA[i]
    if stringA[i+1] == letter:
        count +=1
    else:
        result += "".join(stringA[i]) + str(count)
        count = 1
        continue

file.close()
print(result)
file = open("seminar_5\\task_5_4_output.txt", "w")
file.write(result)
file.close()

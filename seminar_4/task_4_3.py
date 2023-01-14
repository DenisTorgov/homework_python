

import random

size  = int(input("Задайте длину случайной последовательности: "))

str = []
for i in range(size):
    str.append(random.randint(0, 5))

print(str)
reducestr = []

#for i in range(len(str)):
#    count = 0
#    for j in range(len(str)):
#       if str[i] == str[j]:
#            count += 1
#    if count == 1:
#            reducestr.append(str[i])

for i in str:
    if str.count(i) == 1:
        reducestr.append(i)

print(reducestr)
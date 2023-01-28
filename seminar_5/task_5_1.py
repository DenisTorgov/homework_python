# Напишите программу, удаляющую из текста все слова,
# содержащие ""абв"".

stringA = "абв пшзяабв в рпыщзь невчннг опабвпм авыолб гач бва пвавас арогбсфв"

stringB = ""
for i in stringA.split():
    print(i)
    if i.find("абв") < 0:
        stringB = stringB + "".join(i) + " "

print(stringB)


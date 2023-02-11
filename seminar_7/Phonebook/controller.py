def loadfile(filename, mode):
    with open(filename, mode) as f:
        for line in f:
            print(line)

def addcontact(filename, mode):
    print('Введите контакт в формате ')
    f = open(filename, mode)
    lines_count = sum(1 for line in f)
    print(lines_count)
    f.seek(0)
    for i in range(lines_count - 1):
        f.readline()
    id = int((f.readline(1)))
    namecontact = input('Введите имя нового контакта ->')
    phonecontact = input('Введите телефон нового контакта ->')
    f.write(f'\n{id + 1} | {namecontact} | {phonecontact}')
    f.seek(0)
    print((f.read()))
    f.close()

def delcontact(filename, mode):
    id = input('Введите номер контакта для удаления -> ')
    f = open(filename, mode)
    lines = f.readlines()
    f.close()
    f = open(filename, 'w+')
    for line in lines:
        if f'{id} |' not in line:
            f.write(line)
    f.seek(0)
    print((f.read()))
    f.close()

def csvconvert(filename, mode):
    f = open(filename, mode)
    lines = f.readlines()
    f.close()
    fcsv = open('seminar_7\\inputphonebook.csv', 'w+')
    for line in lines:
        line_str = ''
        line = line.rstrip('\n').split('|')
        for i in range(len(line)):
            line[i] = line[i].strip()
            fcsv.write(line[i] + '; ')
        fcsv.write('\n')

csvconvert('seminar_7\\inputphonebook.txt', 'r')
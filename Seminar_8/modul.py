import csv
def find_personal(key):
    with open('Seminar_8\\members.csv', 'r') as file:
        data = file.read().split('\n')
        for i in data:
            if i.lower().count(key):
                id, name, surname, borndate, branch, salary = i.split(';')
                print(f'Match found {id} {name} {surname}\n{borndate}\n{branch}\n{salary}')
        return 'End of search'

def new_personal(card):
    name, surname, borndate, branch, salary = card
    with open('Seminar_8\\members.csv', 'r+') as data:
        id = len(data.read().split('\n'))
        member = f'{id};{name};{surname};{borndate};{branch};{salary}\n'
        data.write(member)
    return 'New member was created'

def del_personal(fired):
    name_check, surname_check = fired
    with open('Seminar_8\\members.csv', 'r+') as data:
        data1 = data.read().split('\n')
        del data1[-1]
        for i in range(len(data1)):
            id, name, surname, borndate, branch, salary = data1[i].split(';')
            if name == name_check and surname == surname_check:
                fired = id, name, surname, borndate, branch, salary
                number = i
        del data1[number]
    with open('Seminar_8\\members.csv', 'w') as data:
        for i in data1:
            data.write(i + '\n')
    return f'{fired} was deleted'

def update_personal(card):
    id_check, name_new, surname_name, borndate_new, branch_new, salary_new = card
    with open('Seminar_8\\members1.csv', 'r+') as data:
        data1 = data.read().split('\n')
        del data1[-1]
        for i in range(len(data1)):
            id, name, surname, borndate, branch, salary = data1[i].split(';')
            if id == id_check:
                update = f'{id};{name_new};{surname_name};{borndate_new};{branch_new};{salary_new}'
                number = i
        data1[number] = update
        print(data1)
    with open('Seminar_8\\members.csv', 'w') as data:
        for i in data1:
            data.write(i + '\n')
    return f"{update}'s entry was updated"

def filter(filter_param):
    with open('Seminar_8\\members.csv', 'r') as file:
        data = file.read().split('\n')
        for i in data:
            if i.lower().count(filter_param):
                id, name, surname, borndate, branch, salary = i.split(';')
                print(f'Match found {id} {name} {surname} {borndate} {branch} {salary}')
        return 'End of search'

def filter_salary(filter_param):
    with open('Seminar_8\\members.csv', 'r') as file:
        data = file.read().split('\n')
        del data[-1]
        for i in data:
            id, name, surname, borndate, branch, salary = i.split(';')
            if int(salary) > int(filter_param):
                print(f'Match found {id} {name} {surname} {borndate} {branch} {salary}')
        return 'End of search'

def export_csv(dict_data):
    with open('data_json.csv', 'w') as csvfile:
        fieldnames = ['name', 'surname', 'position', 'salary']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(dict_data)

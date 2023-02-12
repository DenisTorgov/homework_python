def show_menu() -> int:
    print("\n" + "=" * 20)
    print("Выберите необходимое действие")
    print("1. Найти сотрудника")
    print("2. Сделать выборку сотрудников по должности")
    print("3. Сделать выборку сотрудников по зарплате")
    print("4. Добавить сотрудника")
    print("5. Удалить сотрудника")
    print("6. Обновить данные сотрудника")
    print("7. Экспортировать данные в формате json")
    print("8. Экспортировать данные в формате csv")
    print("9. Закончить работу")
    return int(input("Введите номер необходимого действия: "))


def find_people():
    return input('Find? ')

def filter():
    return input('Filter parameter: ')

def filter_salary():
    return input('Find a personal with salary above: ')

def add_new_personal():
    name = input('Name: ')
    surname = input('Surname: ')
    borndate = input('Date of Birth: ')
    branch = input('Branch of science: ')
    salary = input('Salary: ')
    return name, surname, borndate, branch, salary

def del_personal():
    name = input('Name: ')
    surname = input('Surname: ')
    return name, surname

def update_personal():
    id = input('Id: ')
    print('Enter new data')
    name = input('Name: ')
    surname = input('Surname: ')
    borndate = input('Date of Birth: ')
    branch = input('Branch of science: ')
    salary = input('Salary: ')
    return id, name, surname, borndate, branch, salary

def info(message):
    print(message)
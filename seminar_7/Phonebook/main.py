# phonebook

import view
import controller

view.wellcome()
action = -1
while action != 0:
    action = int(input(view.nextmessage()))
    if action == 1:
        controller.loadfile('seminar_7\\inputphonebook.txt', 'r+')
    elif action == 2:
        controller.addcontact('seminar_7\\inputphonebook.txt', 'r+')
    elif action == 3:
        controller.delcontact('seminar_7\\inputphonebook.txt', 'r')
        print('ok3')

    elif action == 5:
        controller.csvconvert('seminar_7\\inputphonebook.txt', 'r')
        print('ok3')
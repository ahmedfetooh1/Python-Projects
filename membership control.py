""""
    Practical Membership control

"""

admins = ['Ahmed','Sameh','Manal','Ali','Ranem']
name = input('Type your name : ').strip().capitalize()

if name in admins :
    print(f'Hello {name} welcome back')
    option = input('Delete(d) or Update(u) your name?').strip().lower()

    if option == 'update' or option == 'u':
        newName = input('Enter your new name :')
        admins[admins.index(name)] = newName
        print(f'Your name {newName} is already updated')

    elif option == 'delete' or option =='d':
        admins.remove(name)
        print('Name deleted')

    else :
        print('Wrong option.')
else:
    status = input('You are not admin.\nDo you want to be admin Y/N ?').strip().lower()

    if status == 'yes' or status == 'y' :
        admins.append(name)
        print(f'You have been added {name} .')
    else :
        print('You are not added')

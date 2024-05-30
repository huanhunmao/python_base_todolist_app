user_action = input('Type add, show , edit,  or exit: ')
user_action = user_action.strip()

if 'add' in user_action:
    todo = user_action[4:]
elif 'show' in user_action:
    with open('todos-delete.txt', 'r') as file:
        todos = file.readlines()
else:
    print('Command  is not valid.')
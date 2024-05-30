while True:
    user_action = input('Enter delete number: ')
    user_action = user_action.strip()

    try:
        # 用户输入的是"delete 2"，那么user_action[7:]会得到" 2"
        number = int(user_action[7:].strip())

        with open('todos-delete.txt', 'r') as file:
            todos = file.readlines()

        index = number - 1
        todo_to_remove = todos[index].strip('\n')
        todos.pop(index)

        with open('todos-delete.txt', 'w') as file:
            file.writelines(todos)

        message = f"Todo {todo_to_remove} was removed from the list"
        print(message)
        print(todos)

    except IndexError:
        print('There is no item  with the number')
    except ValueError:
        print('Invalid input. Please enter a valid number after "delete".')
    except FileNotFoundError:
        print('The file todos-delete.txt does not exist.')

with open('todos-delete.txt', 'r') as file:
    todos = file.readline()

with open('todos-delete.txt', 'w') as file:
    file.writelines(todos)
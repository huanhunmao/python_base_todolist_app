# 定义函数
def get_todos(filepath = 'todos-delete.txt'):
    with open(filepath, 'r') as local_file:
        todos_local = local_file.readlines()
        return todos_local


def write_todos(todos_arg, filepath = 'todos-delete.txt'):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

todos = get_todos('todos-delete.txt')

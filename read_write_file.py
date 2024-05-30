todo = input('Enter a todo: ')

file = open('todos.txt', 'r')
todos = file.readline()

# 将读取的内容转换为列表（假设文件内容是一个字符串形式的列表）
todos_list = eval(todos)
file.close()

todos_list.append(todo)

file = open('todos.txt', 'w')

# 将列表写回文件
file.writelines(str(todos_list))
file.close()

new_todos = [item.strip('\n') for item in todos]
print(new_todos)
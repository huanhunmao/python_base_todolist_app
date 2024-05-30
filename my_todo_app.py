import PySimpleGUI as sg
from def_func import get_todos, write_todos

label = sg.Text('Type in a to-do')
input_box = sg.Input(key='todo', tooltip='Enter todo')  # 添加一个key参数来关联输入框
add_button = sg.Button('Add')

layout = [[label], [input_box, add_button], [sg.Text(size=(40, 10), key='todos')]]  # 添加一个文本框用来显示待办事项

window = sg.Window('My To-Do App', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:  # 添加窗口关闭事件处理
        break
    if event == 'Add':
        todos = get_todos()
        new_todo = values['todo'] + '\n'
        todos.append(new_todo)
        write_todos(todos)
        window['todos'].update(value=''.join(todos))  # 更新文本框内容

window.close()

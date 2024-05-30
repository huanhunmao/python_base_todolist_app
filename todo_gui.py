import streamlit as st
import def_func

# 导入 def_func.py 中的函数
todos = def_func.get_todos()


def add_todo():
    new_todo = st.session_state['new_todo']
    if new_todo.strip():
        todos.append(new_todo)
        def_func.write_todos(todos)
        # 如果第一次调用，则创建新的文本输入框，否则更新现有的文本输入框
        if 'new_todo_input' not in st.session_state:
            st.session_state['new_todo_input'] = st.empty()
        st.session_state['new_todo_input'].text_input(label='', placeholder='Add new todo ...', key='new_todo')


st.title('My Todo App')
st.subheader('This is my todo list app')
st.write('This app is to increase your ideas')

for index, todo in enumerate(todos):
    print('todo',todo)
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        # 删除选中的待办事项
        todos.pop(index)
        def_func.write_todos(todos)
        st.experimental_rerun()

# 使用 st.text_area 和 st.button 实现添加新待办事项的功能
new_todo = st.text_area(label='Add new todo ...', key='new_todo')
if st.button('Add'):
    add_todo()

# 使用这个命令 打开
# streamlit run todo_gui.py

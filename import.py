from def_func import get_todos, write_todos
import time

todos = get_todos()

now = time.strftime('%b %d, %Y %H:%M:%S')
print('It is', now) # It is May 30, 2024 11:37:27
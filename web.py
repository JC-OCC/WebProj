import streamlit as st
import functions


def add_todo():
    print("add_todo")
    todo = st.session_state["new_todo"]
    todos.append(todo + '\n')
    functions.write_todos(todos)
    print(todos)

todos = functions.get_todos()

st.title("My Todo App") 

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo,key = f"test{index}")
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        st.session_state.text_input = ''
        todo = st.rerun()
        
st.text_input(label="",placeholder="add a new todo...", on_change=add_todo, key="new_todo")

st.session_state
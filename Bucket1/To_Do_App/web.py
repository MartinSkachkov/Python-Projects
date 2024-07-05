import streamlit as st
import functions

todos = functions.get_todos()


def add_new_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    # st.rerun() is called implicitly by the framework to update ui


st.title("To Do App")
st.subheader("Tasks to be done for the day:")

for idx, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=idx)
    if checkbox == True:
        todos.pop(idx)
        functions.write_todos(todos)
        del st.session_state[idx]
        st.rerun()  # ui update

# next line is executed only when the user presses enter after entering text in the text box, otherwise it is skipped
st.text_input(label="", placeholder="Add new task...", on_change=add_new_todo, key="new_todo")

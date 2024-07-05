FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    with open(filepath, "r") as file_todos:
        list_todos = file_todos.readlines()
    return list_todos


def write_todos(todos_args, filepath=FILEPATH):
    with open(filepath, "w") as file_todos:
        # It writes each string in the iterable todos_args to the file,
        # without adding any additional characters (like newlines) between the lines.
        file_todos.writelines(todos_args)

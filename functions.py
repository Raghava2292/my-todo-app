FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """
    Get the todos text file, reads it and makes a list with its contents
    :param filepath:
    :return:
    """
    with open(filepath, 'r') as file:
        return file.readlines()


def write_todos(file_list, filepath=FILEPATH):
    """
    Takes the todos list and makes a text file with the list contents
    :param file_list:
    :param filepath:
    :return:
    """
    with open(filepath, 'w') as file:
        file.writelines(file_list)

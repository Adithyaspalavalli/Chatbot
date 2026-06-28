# memory.py

user_memory = {}


def save_memory(key, value):

    user_memory[key] = value



def get_memory(key):

    return user_memory.get(key)



def show_memory():

    return user_memory
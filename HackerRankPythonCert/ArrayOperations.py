# if __name__ == '__main__':
    # N = int(input())

def handle_append(command_string, arr_integer):
    arr_command_string = str(command_string).split(" ")
    arr_integer.append(arr_command_string[1])

def handle_print(arr_integer):
    print(arr_integer)

def handle_remove(command_string, arr_integer):
    arr_command_string = str(command_string).split(" ")
    arr_integer.remove(arr_command_string[1])

def interpret_command(command_string, arr_integer):
    if str(command_string).startswith('append'):
        handle_append(command_string,arr_integer)
    elif str(command_string).startswith('print'):
        handle_print(arr_integer)
    elif str(command_string).startswith('remove'):
        handle_remove(command_string,arr_integer)

arr_integer = []
arr_commands = ['append 1', 'append 55','print','remove 1','print']
for command_string in arr_commands:
    interpret_command(command_string, arr_integer)
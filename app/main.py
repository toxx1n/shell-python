import sys
import os
import subprocess

def exit_handler(arguments):
    sys.exit()

def echo_handler(arguments):
    output = ' '.join(arguments)
    print(output)

def type_handler(arguments):
    if not arguments:
        return
    command_to_check = arguments[0]

    if command_to_check in DISPATCHER:
        print(f'{command_to_check} is a shell builtin')
    else:
        found = False
        for path in PATHS:
            full_path = os.path.join(path,command_to_check)
            if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
                print(f'{command_to_check} is {full_path}')
                found = True
                break
        if not found:
            print(f"{command_to_check}: not found")

def pwd_handler(arguments):
    print(os.getcwd())


PATHS = os.environ.get('PATH','').split(os.pathsep)

DISPATCHER = {
        'exit': exit_handler,
        'echo': echo_handler,
        'type': type_handler,
        'pwd': pwd_handler,
    }


def read_command():
    cmd = input('$ ').strip()
    if not cmd:
        return None, None
    tokens = cmd.split()
    command = tokens[0]
    arguments = tokens[1:]
    return command, arguments

def dispatch_command(command, arguments):
    if not command:
        return
    
    if command in DISPATCHER:
        DISPATCHER[command](arguments)
    else:
        found = False
        for path in PATHS:
            full_path = os.path.join(path,command)
            if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
                found = True
                break
        if found:
            subprocess.run([command] + arguments)
        else:
            print(f'{command}: command not found')


def main():
    while True:
        command, arguments = read_command()
        dispatch_command(command, arguments)


    



if __name__ == "__main__":
    main()

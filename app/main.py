import sys


def main():
    
    builtin = ['exit','echo','type']
    while True:
        cmd = input('$ ').strip()

        if cmd == 'exit':
            break
        elif cmd[:4] == 'echo':
            print(cmd[5:])
        elif cmd[:4] == 'type':
            command_to_check = cmd[5:]
            if command_to_check in builtin:
                print(f"{command_to_check} is a shell builtin")
            else:
                print(f"{command_to_check} not found")
        else:
            print(f"{cmd}: command not found")

if __name__ == "__main__":
    main()

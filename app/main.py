import sys


def main():
    
    while True:
        cmd = input('$ ').strip()

        if cmd == 'exit':
            break
        elif cmd[:4] == 'echo':
            print(cmd[5:])
        else:
            print(f"{cmd}: command not found")

if __name__ == "__main__":
    main()

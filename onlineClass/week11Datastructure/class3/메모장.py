'''
notepad 함수를 작성하세요.

abcdef
3
P g
L
P z

'''


def notepad(s, commands):
    left = list(s)
    right = []

    for line in commands:
        command = line.split()
        action = command[0]
        if action == "L":
            if len(left) > 0:
                v = left.pop()
                right.append(v)
        elif action == 'R':
            if len(right) > 0:
                v = right.pop()
                left.append(v)
        elif action == "D":
            if len(left) > 0:
                left.pop()
        elif action == "P":
            left.append(command[1])
    result = left+right[::-1]

    return "".join(result)


def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    s = input()

    n = int(input())

    commands = []

    for i in range(n):
        commands.append(input())

    print(notepad(s, commands))


if __name__ == "__main__":

    main()

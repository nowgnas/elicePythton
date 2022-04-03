from stack import Stack


def main():
    stack = Stack()

    '''
    테스트를 위한 코드입니다.
    '''

    n = int(input())

    for i in range(n):
        temp = [int(v) for v in input().split()]

        x = temp[0]

        if x == 1:
            stack.push(temp[1])
        elif x == 2:
            stack.pop()
        elif x == 3:
            print(stack.size())
        elif x == 4:
            print(stack.empty())
        elif x == 5:
            print(stack.top())


if __name__ == "__main__":
    main()

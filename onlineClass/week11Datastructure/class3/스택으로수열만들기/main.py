from stack_sequence import is_stack_sequence


def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    n = int(input())

    for i in range(n):
        myList = [int(v) for v in input().split()]

        print(is_stack_sequence(myList))


if __name__ == "__main__":
    main()

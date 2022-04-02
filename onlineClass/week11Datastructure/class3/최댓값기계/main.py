from maxMachine import maxMachine

'''
9
0 1
0 2
0 4
0 5
2
1 5
2
1 2
2
'''


def main():

    myMachine = maxMachine()

    '''
    테스트를 위한 코드입니다.
    '''

    n = int(input())

    for i in range(n):
        line = [int(v) for v in input().split()]
        if line[0] == 0:
            myMachine.addNumber(line[1])
        elif line[0] == 1:
            myMachine.removeNumber(line[1])
        elif line[0] == 2:
            print(myMachine.getMax())


if __name__ == "__main__":
    main()

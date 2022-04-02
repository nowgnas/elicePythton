from beads import processBeads
'''
3
1 0
2 1
3 0

'''


def main():
    '''
    이 곳은 수정하지 마세요.
    '''

    n = int(input())

    myList = []

    for i in range(n):
        myList.append([int(v) for v in input().split()])

    print(*processBeads(myList))


if __name__ == "__main__":
    main()

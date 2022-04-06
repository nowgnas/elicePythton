'''
getHeight 함수를 작성하세요.
'''


def getHeight(myTree):
    '''
    myTree의 높이를 반환하는 함수를 작성하세요.
    '''
    # 왼쪽 서브 트리의 높이 구하기
    # 오른쪽 서브 트리 높이 구하기
    # 두개 높이 비교
    # 왼쪽 서브 높으면 +1(루트노드)
    if myTree == None:
        return 0
    else:
        return 1 + max(getHeight(myTree.left), getHeight(myTree.right))


def main():
    myTree = getHeight(None, None, None)

    n = int(input())

    for i in range(n):
        myList = [int(v) for v in input().split()]

        if myList[1] == -1:
            myList[1] = None

        if myList[2] == -1:
            myList[2] = None

        myTree.addNode(myList[0], myList[1], myList[2])

    print(getHeight(myTree))


if __name__ == "__main__":
    main()

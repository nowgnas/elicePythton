'''
preorder, inorder, postorder 함수를 구현하세요.
'''


def preorder(tree):
    '''
    tree를 전위순회 하여 리스트로 반환하는 함수를 작성하세요.
    '''
    # 루트 + 왼쪽 전위 순회 + 오른쪽 전위 순회
    result = []
    result.append(tree.index)
    if tree.left != None:
        result += preorder(tree.left)

    if tree.right != None:
        result += preorder(tree.right)

    return result


def inorder(tree):
    '''
    tree를 중위순회 하여 리스트로 반환하는 함수를 작성하세요.
    '''
    result = []
    if tree.left != None:
        result += inorder(tree.left)
    result.append(tree.index)

    if tree.right != None:
        result += inorder(tree.right)

    return result


def postorder(tree):
    '''
    tree를 후위순회 하여 리스트로 반환하는 함수를 작성하세요.
    '''
    result = []
    if tree.left != None:
        result += postorder(tree.left)

    if tree.right != None:
        result += postorder(tree.right)
    result.append(tree.index)

    return result


'''
5
1 2 3
2 4 5
3 -1 -1
4 -1 -1
5 -1 -1
'''


def main():
    myTree = Tree(None, None, None)

    n = int(input())

    for i in range(n):
        myList = [int(v) for v in input().split()]

        if myList[1] == -1:
            myList[1] = None

        if myList[2] == -1:
            myList[2] = None

        myTree.addNode(myList[0], myList[1], myList[2])

    print(*preorder(myTree))
    print(*inorder(myTree))
    print(*postorder(myTree))


if __name__ == "__main__":
    main()

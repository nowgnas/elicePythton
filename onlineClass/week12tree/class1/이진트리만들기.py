class Tree:
    # 어떤 트리의 루트 노드를 가지고 있다
    def __init__(self, i, l, r):
        self.index = i
        self.left = l
        self.right = r

    def addNode(self, i, l, r):
        '''
        트리 내의 정점 i에 대하여 왼쪽자식을 l, 오른쪽 자식을 r로
        설정해주는 함수를 작성하세요.
        '''
        # 루트 노드에 대한 처리
        if self.index == None or self.index == i:
            self.index = i
            self.left = Tree(l, None, None) if l != None else None
            self.right = Tree(r, None, None) if r != None else None

            return True
        else:
            flag = False
            if self.left != None:
                flag = self.left.addNode(i, l, r)
            if flag == False and self.right != None:
                flag = self.right.addNode(i, l, r)
            return flag


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

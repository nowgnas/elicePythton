'''
BFS 함수를 구현하세요.
'''

from queue import Queue


def BFS(tree):
    '''
    tree를 너비 우선 탐색으로 순회하여 리스트로 반환하는 함수를 작성하세요.
    bfs는 큐를 사용
    '''
    q = Queue()
    q.put(tree)

    result = []

    # q에 뭔가 들어있으면 반복

    while len(q.queue) > 0:
        cur = q.get()
        if cur == None:
            continue

        result.append(cur.index)  # 방문
        q.put(cur.left)
        q.put(cur.right)

    return result


def main():
    myTree = BFS(None, None, None)

    n = int(input())

    for i in range(n):
        myList = [int(v) for v in input().split()]

        if myList[1] == -1:
            myList[1] = None

        if myList[2] == -1:
            myList[2] = None

        myTree.addNode(myList[0], myList[1], myList[2])

    print(*BFS(myTree))


if __name__ == "__main__":
    main()

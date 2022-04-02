from orderManager import orderManager

'''
10
1 1
1 2
1 4
2 2
3 1
3 4
1 2
2 1
1 1
3 2
'''


def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    line = [int(v) for v in input().split()]
    m = line[0]

    manager = orderManager()

    for i in range(m):
        line = [int(v) for v in input().split()]

        if line[0] == 1:
            manager.addOrder(line[1])

        elif line[0] == 2:
            manager.removeOrder(line[1])

        elif line[0] == 3:
            myOrder = manager.getOrder(line[1])

            if myOrder == -1:
                print("-1")
            else:
                print(str(manager.getOrder(line[1])))


if __name__ == "__main__":
    main()

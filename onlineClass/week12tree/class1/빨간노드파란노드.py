from platform import node


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    nodes = []
    for _ in range(n):
        a, b = map(int, input().split())
        nodes.append((a, b))
    print(nodes)


'''

7
0 1 0 0 0 2 0
3 6
5 2
7 5
4 2
1 2
3 1

'''
if __name__ == "__main__":
    main()

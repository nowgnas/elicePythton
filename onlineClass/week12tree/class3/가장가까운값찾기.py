import math
import sys


def getNearest(data, m):
    '''
    n개의 숫자가 list로 주어지고, 숫자 m이 주어질 때, n개의 숫자 중에서 m과 가장 가까운 숫자를 반환하는 함수를 작성하세요.
    '''

    minDistance = 100000
    answer = []
    distance = 0
    for i in data:
        distance = abs(i-m)
        if distance < minDistance:
            minDistance = distance
            answer.append((i, distance))
    return min(answer, key=lambda x: x[1])[0]


def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    data = [int(x) for x in input().split()]
    m = int(input())

    print(getNearest(data, m))


if __name__ == "__main__":
    main()

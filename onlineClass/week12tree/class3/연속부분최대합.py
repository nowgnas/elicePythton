import sys


def getSubsum(data):
    '''
     n개의 숫자가 list로 주어질 때, 그 연속 부분 최대합을 반환하는 함수를 작성하세요.

     분할정복으로 풀이 
    '''
    # 리스트에 값이 한개인 경우 처리
    n = len(data)
    if n == 1:
        return data[0]

    '''
    왼쪽 오른쪽 양쪽
    '''
    mid = n//2

    # 왼쪽 부분 최대합
    left = getSubsum(data[:mid])
    # 오른쪽 부분 최대 합
    right = getSubsum(data[mid:])

    Sum = 0
    leftSum = 0
    rightSum = 0

    # 왼쪽
    for i in range(mid-1, -1, -1):
        Sum += data[i]
        leftSum = max(Sum, leftSum)
    Sum = 0
    for i in range(mid, n):
        Sum += data[i]
        rightSum = max(Sum, rightSum)

    return max([left, right, leftSum+rightSum])


def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    data = [int(x) for x in input().split()]

    print(getSubsum(data))


if __name__ == "__main__":
    main()

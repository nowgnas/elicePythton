import sys


def binarySearch(data, m):
    '''
    n개의 숫자 중에서 m이 존재하면 "Yes", 존재하지 않으면 "No"를 반환하는 함수를 작성하세요.
    '''
    def bs(arr, target, start, end):
        if start > end:
            return None
        mid = (start+end)//2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return bs(arr, target, start, mid-1)
        else:
            return bs(arr, target, mid+1, end)

    result = bs(data, m, 0, len(data)-1)
    if result == None:
        return "No"
    else:
        return "YES"


def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    data = [int(x) for x in input().split()]
    m = int(input())

    print(binarySearch(data, m))


if __name__ == "__main__":
    main()

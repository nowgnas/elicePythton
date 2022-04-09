import sys


def numSubstr(A, B):
    '''
    B가 A에 포함되어 있는 횟수를 반환하는 함수를 작성하세요.
    '''
    pattern = len(B)
    step = len(A)
    cnt = 0

    for i in range(step-pattern+1):
        if A[i:i+pattern] == B:
            cnt += 1

    return cnt


def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    A = input()
    B = input()

    print(numSubstr(A, B))


if __name__ == "__main__":
    main()

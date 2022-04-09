LIMIT_NUMBER = 1000000007


def getPower(m, n):
    '''
    m^n 을 LIMIT_NUMBER로 나눈 나머지를 반환하는 함수를 작성하세요.
    입력 크기가 커서 단순하게 곱해서는 안된다 
    '''

    if n == 0:
        return 1
    elif n % 2 == 0:
        temp = getPower(m, n//2)
        return (temp*temp) % LIMIT_NUMBER
    else:
        temp = getPower(m, (n-1)//2)
        return (temp*temp*m) % LIMIT_NUMBER


def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    myList = [int(v) for v in input().split()]

    print(getPower(myList[0], myList[1]))


if __name__ == "__main__":
    main()

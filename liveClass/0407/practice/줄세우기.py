def lining(n):
    '''
    n명의 학생을 일렬로 줄세우는 경우의 수를 1,000,000,007 로 나눈 나머지를 반환하는 함수를 작성하세요.
    '''

    Table = [0 for i in range(n+1)]

    Table[1] = 2
    Table[2] = 3

    # Table 에 각각 값을 넣어줍시다

    return Table[n]


def main():

    data = int(input())

    print(lining(data))


if __name__ == "__main__":
    main()

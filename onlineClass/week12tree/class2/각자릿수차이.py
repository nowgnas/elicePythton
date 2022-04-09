def fillString(string, length):
    needToFill = length-len(string)
    newString = '.'*needToFill+string
    return newString


def diffDigit(a, b):
    '''
    a, b의 서로 다른 자리수의 개수를 반환한다
    '''
    a, b = str(a), str(b)
    maxLength = max(len(a), len(b))
    if len(a) < maxLength:
        a = fillString(a, maxLength)
    if len(b) < maxLength:
        b = fillString(b, maxLength)

    result = 0
    for _a, _b in zip(a, b):
        if _a != _b:
            result += 1
        else:
            continue

    return result


def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    a = int(input())
    b = int(input())

    print(diffDigit(a, b))


if __name__ == "__main__":
    main()

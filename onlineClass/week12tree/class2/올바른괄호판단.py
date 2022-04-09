from tabnanny import check


def checkParen(p):
    '''
    괄호 문자열 p의 쌍이 맞으면 "YES", 아니면  "NO"를 반환
    기저조건 처리 
    p에서 인접한 괄호쌍을 찾아 제거 
    checkParen()함수에 다시 물어본다 
    '''

    if len(p) == 0:
        return 'YES'
    elif len(p) == 1:
        return "No"

    for item in range(len(p)-1):
        if p[item] == '(' and p[item+1] == ')':
            q = p[:item] + p[item+2:]
            return checkParen(q)

    return "NO"


def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    x = input()
    print(checkParen(x))


if __name__ == "__main__":
    main()

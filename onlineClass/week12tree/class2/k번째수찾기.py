def findKth(myInput, k):
    '''
    매 순간마다 k번째로 작은 원소를 리스트로 반환합니다.
    '''
    answer = []
    result = []
    for item in myInput:
        result.append(item)
        if len(result) < k:
            answer.append(-1)
        else:
            single_result = result[:]
            single_result.sort()
            answer.append(single_result[k-1])

    return answer


def main():
    '''
    테스트를 하고싶으면, 아래 부분을 수정합니다.
    '''

    firstLine = [int(x) for x in input("n과 k를 입력하세요 (예시:10 3): ").split()]
    myInput = [int(x) for x in input(
        "n개의 숫자를 차례대로 입력하세요 (예시:1 9 8 5 2 3 5 6 2 10): ").split()]

    print('정렬 결과: ', *findKth(myInput, firstLine[1]))


if __name__ == "__main__":
    main()

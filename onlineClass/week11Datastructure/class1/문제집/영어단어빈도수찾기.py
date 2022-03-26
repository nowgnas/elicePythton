
import os


root = os.getcwd()
filePath = f'{root}/onlineClass/week11Datastructure/class1/문제집'

txt = '/corpus.txt'


def filter_by_text(text):
    # 지시사항을 참고하여 코드를 작성하세요.
    answer = []
    with open(filePath+txt) as file:
        for item in file:
            word, cnt = item.strip().split(',')
            if word.startswith(text):
                answer.append((word, cnt))

    return answer


# 값을 확인하기 위한 코드입니다. 값을 변경해가며 테스트해 보세요!
print(filter_by_text('a'))

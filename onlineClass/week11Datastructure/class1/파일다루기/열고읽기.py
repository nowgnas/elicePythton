import os


root = os.getcwd()
filePath = f'{root}/onlineClass/week11Datastructure/class1/파일다루기'


# 텍스트 파일을 불러옵니다.
filename = 'corpus.txt'


def pring_lines(filename):
    lineNum = 1
    with open(f'{filePath}/{filename}', 'r') as file:
        for item in file:
            print(f'{lineNum} {item}')
            lineNum += 1


# 아래 주석을 해제하고 결과를 확인해보세요.
pring_lines(filename)

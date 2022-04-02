import os


root = os.getcwd()
filePath = f'{root}/onlineClass/week11Datastructure/class1/파일다루기'


# 텍스트 파일을 불러옵니다.
filename = 'corpus.txt'


def import_as_tuple(filename):
    tuples = []
    with open(filePath+'/'+filename) as file:
        for line in file:
            word, cnt = line.strip().split(',')
            tuples.append((word, cnt))

    return tuples


# 아래 주석을 해제하고 결과를 확인해보세요.
print(import_as_tuple(filename))

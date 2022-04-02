# 아래 코드는 문제 해결을 위해 기본적으로 제공되는 코드입니다. 수정하지 마세요!
import csv

file = '/mnt/f/elicepy/onlineClass/week11Datastructure/class2/TEDAnalysis/ted.csv'


def get_popular_speaking(n):
    # 지시사항을 참고하여 코드를 작성하세요.
    answer = []
    with open(file) as files:
        reader = csv.reader(files, delimiter=',')

        for row in reader:
            if int(row[16]) > n:
                answer.append((row[14], int(row[16])))

    return sorted(answer, key=lambda x: x[1], reverse=True)


# 값을 확인하기 위한 코드입니다. 값을 변경해가며 테스트해 보세요!
print(get_popular_speaking(40000000))

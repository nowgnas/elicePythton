# 리스트와 집합을 이용해 문제를 해결할 수 있습니다.
import collections
import itertools


word = input()

slist = []
lenth = len(word)
# 입력된 문자열을 인덱싱하여 원소들에 대한 부분 집합을 구해 배열에 넣습니다.
for i in range(lenth, 0, -1):
    for j in range(i):
        count = lenth - i + 1
        subset = word[j:j+count]
        slist.append(subset)
# 배열에서 중복된 문자는 제거합니다.
slist = list(set(slist))

print(len(slist)-1)

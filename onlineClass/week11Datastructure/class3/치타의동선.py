# 리스트를 이용해 문제를 해결할 수 있습니다.
import sys
# Counter는 카운팅을 쉽게 할 수 있게 돕는 라이브러리입니다.
# https://docs.python.org/ko/3/library/collections.html#collections.Counter
from collections import Counter

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
adict = Counter(alpha)
sen = sys.stdin.readline().strip()
stack = []
count = 0
for i in sen:
    adict.update(i)
    if adict.get(i) == 3:
        # 알파벳 겹치게 되는 경우가 몇 개인지를 계산하고, 계산된 것은 제거합니다.
        count += len(stack) - stack.index(i) - 1
        stack.remove(i)
    else:
        # 리스트의 마지막에 알파벳을 넣어 겹치는 경우를 확인합니다.
        stack.append(i)
print(count)

'''
https://jennymunjung.notion.site/c0dde7378aa74e1590554af3208e1891
'''
from collections import deque

n, k, m = map(int, input().split())
que = deque([i for i in range(1, n+1)])
count = 0

while que:
    que.rotate(-(k-1))
    a = que.popleft()
    count += 1
    if a == m:
        break

print(count)

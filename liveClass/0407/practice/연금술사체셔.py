import sys

'''
5
3 10 2 8 14
'''
import heapq

metalNum = int(input())

metalList = list(map(int, input().split()))

answer = 1
heapq.heapify(metalList)

while len(metalList) >= 2:
    temp_1 = heapq.heappop(metalList)
    temp_2 = heapq.heappop(metalList)
    answer = answer*temp_1*temp_2
    heapq.heappush(metalList, temp_1*temp_2)

print(answer % 1000007)

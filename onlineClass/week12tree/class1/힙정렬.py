'''
heapSort 함수를 구현하세요.
'''


import heapq


class PriorityQueue:
    '''
    우선순위 큐를 힙으로 구현합니다
    '''

    def __init__(self):
        self.data = [0]

    def push(self, value):
        '''
        우선순위 큐에 value를 삽입합니다.
        '''

        self.data.append(value)
        index = len(self.data)-1

        # 마지막으로 삽입한 값이 루트 노드가 되면 종료
        while index != 1:
            # 몫연산으로 부모 노드의 인덱스를 가져올 수 있는 것이 이진트리의 특성이다
            if self.data[index//2] > self.data[index]:
                temp = self.data[index]
                self.data[index] = self.data[index//2]
                self.data[index//2] = temp

                index = index//2
            else:
                break

    def pop(self):
        '''
        우선순위가 가장 높은 원소를 제거합니다.
        '''

        if len(self.data) == 1:
            return

        # 마지막 노드를 루트 노드 자리로 이동한다
        self.data[1] = self.data[-1]
        self.data.pop()

        index = 1
        while True:
            priority = -1
            # 1. 아무런 자식이 없는 경우
            if len(self.data)-1 < index * 2:
                break
            # 2. 왼쪽 자식만 있는 경우
            elif len(self.data) - 1 < index*2 + 1:
                priority = index*2
            else:
                if self.data[index*2] < self.data[index*2+1]:
                    priority = index*2
                else:
                    priority = index*2+1
            if self.data[index] > self.data[priority]:
                temp = self.data[index]
                self.data[index] = self.data[priority]
                self.data[priority] = temp

                index = priority
            else:
                break

    def top(self):
        '''
        우선순위가 가장 높은 원소를 반환합니다. 만약 우선순위 큐가 비어있다면 -1을 반환합니다.
        '''

        if len(self.data) == 1:
            return -1
        else:
            return self.data[1]


def heapSort(items):
    '''
    items에 있는 원소를 heap sort하여 리스트로 반환하는 함수를 작성하세요.

    단, 이전에 작성하였던 priorityQueue를 이용하세요.
    '''

    result = []
    pq = PriorityQueue()
    for i in items:
        pq.push(i)
    for i in range(len(items)):
        result.append(pq.top())
        pq.pop()

    return result


def main():
    '''
    Do not change this code
    '''

    line = [int(x) for x in input().split()]

    print(*heapSort(line))


if __name__ == "__main__":
    main()

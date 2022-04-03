'''
함수 processOrder를 구현하세요.
'''


class Queue:
    '''
    List를 이용하여 다음의 method들을 작성하세요.
    '''

    def __init__(self):
        '''
        큐 myQueue을 만듭니다.
        '''
        self.myQueue = []

    def push(self, n):
        '''
        queue에 정수 n을 넣습니다.
        '''
        self.myQueue.append(n)

    def pop(self):
        '''
        queue에서 가장 앞에 있는 정수를 제거합니다. 만약 queue에 들어있는 값이 없을 경우에는 아무 일도 하지 않습니다. 
        '''
        if self.empty() == 1:
            return
        else:
            self.myQueue.pop(0)

    def size(self):
        '''
        queue에 들어 있는 정수의 개수를 return 합니다.
        '''
        return len(self.myQueue)

    def empty(self):
        '''
        queue이 비어있다면 1, 아니면 0을 return 합니다.
        '''
        if self.size() == 0:
            return 1
        else:
            return 0

    def front(self):
        '''
        queue의 가장 앞에 있는 정수를 return 합니다. 만약 queue에 들어있는 값이 없을 경우에는 -1을 return 합니다.
        '''
        if self.empty() == 1:
            return -1
        else:
            return self.myQueue[0]

    def back(self):
        '''
        queue의 가장 뒤에 있는 정수를 return 합니다. 만약 queue에 들어있는 값이 없을 경우에는 -1을 return 합니다.
        '''
        if self.empty() == 1:
            return -1
        else:
            return self.myQueue[-1]


class orderInfo:
    '''
    이 부분은 수정하지 마세요.
    '''

    def __init__(self, t, d, v):
        self.time = t
        self.duration = d
        self.vip = v


def selectQueue(normalQueue, vipQueue, time, orders):
    normalIndex = normalQueue.front()
    vipIndex = vipQueue.front()

    if vipIndex == -1:
        return normalQueue
    if normalIndex == -1:
        return vipQueue

    # 밀린 작업이 normal에도 없고 vip에도 없는 경우
    # 빨리 도착한 주문을 처리한다
    if time < orders[normalIndex].time and time < orders[vipIndex].time:

        if orders[vipIndex].time <= orders[normalIndex].time:
            return vipQueue
        else:
            return normalQueue

    # 밀린 작업이 normal 에만 있는경우
    if time >= orders[normalIndex].time and time < orders[vipIndex].time:
        return normalQueue
    if time >= orders[vipIndex].time and time < orders[normalIndex].time:
        return vipQueue

    # 밀린 작업이 normal, vip에도 있는 경우
    return vipQueue


def processOrder(orders):
    '''
    주문 정보가 주어질 때, 주문이 처리되는 순서를 반환합니다.
    '''

    result = []

    normalQueue = Queue()
    vipQueue = Queue()

    jobEndTime = 0
    curTime = -1

    for i in range(len(orders)):
        curTime = orders[i].time

        if orders[i].vip == 0:
            normalQueue.push(i)
        else:
            vipQueue.push(i)

        while jobEndTime <= curTime and not(normalQueue.empty() == 1 and vipQueue.empty() == 1):
            # normal이나 vip를 선택한다
            targetQueue = selectQueue(
                normalQueue, vipQueue, jobEndTime, orders)

            index = targetQueue.front()
            jobEndTime = max(
                jobEndTime, orders[index].time) + orders[index].duration

            result.append(index+1)
            targetQueue.pop()

        while not(normalQueue.empty() == 1 and vipQueue.empty() == 1):
            # normal이나 vip를 선택한다
            targetQueue = selectQueue(
                normalQueue, vipQueue, jobEndTime, orders)

            index = targetQueue.front()
            jobEndTime = max(
                jobEndTime, orders[index].time) + orders[index].duration

            result.append(index+1)
            targetQueue.pop()

    return result


def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    p = int(input())

    orders = []

    for i in range(p):
        myList = [int(v) for v in input().split()]

        orders.append(orderInfo(myList[0], myList[1], myList[2]))

    print(*processOrder(orders))


if __name__ == "__main__":
    main()

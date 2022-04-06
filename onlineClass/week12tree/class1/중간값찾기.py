import heapq


def find_mid(nums):
    '''
    n개의 정수들을 담고 있는 배열 nums가 매개변수로 주어집니다.
    nums의 각 정수들이 차례대로 주어질 때, 매 순간마다 
    "지금까지 입력된 수 중에서 중간값"을 리스트로 저장하여 반환하세요.
    '''
    n = len(nums)
    result = []
    l = []  # 최대 힙
    r = []  # 최소힙

    for i in range(n):
        x = nums[i]

        if not l or not r:
            heapq.heappush(l, -x)
        else:
            if x >= -l[0]:
                heapq.heappush(r, x)
            else:
                heapq.heappush(l, -x)
        # 두 힙의 크기를 조절
        # l과 r이 가지고 있는 자료의 개수는 같아야 한다
        # 총 자료의 개수가 홀수라면, l이 하나 더 많이 들고 있어야 한다
        while not (len(l) == len(r) or len(l) == len(r)+1):
            if len(l) > len(r):
                # l이 들고 있는 개수가  r의 개수보다 2개 이상이다
                # l에서 값을 뽑아 r에 넣어준다
                heapq.heappush(r, -heapq.heappop(l))
            else:
                # r이 l보다 많이 가지고 있는 경우
                heapq.heappush(l, -heapq.heappop(r))
        result.append(-l[0])

    return result


def main():
    '''
    테스트를 위한 코드입니다.
    '''

    n = int(input())

    nums = [int(v) for v in input().split()]

    print(*find_mid(nums))


if __name__ == "__main__":
    main()

# functools를 import하세요.
import functools

import itertools


def main():
    # iterable 객체를 입력받으세요.
    test = [1, 2, 3, 4]
    print(functools.reduce(lambda x, y: x + y, test))  # 10

    lst = map(int, input().split())

    print(functools.reduce(lambda x, y: x * y if x < y else x//y, lst))

#     lambda x,y : x *y if x < y else x//y

#     if x < y :
#         return x*y
#     else: # x>=y
#         return x//u

    # 입력으로 주어지는 iterable 객체에 지시사항에서 주어진 연산을 적용하세요.


if __name__ == "__main__":
    main()

# itertools 라이브러리를 불러오세요.
import itertools


def main():
    # `3 3 3` 을 멤버로 가지는 iterator를 생성하세요.
    # > x = itertools.count()  # 무한으로 생성
    # for item in x:
    # x = itertools.combinations([1, 2, 3], 2)
    # print(list(x))

    # # 생성한 iterator의 값을 누적한 iterator를 생성하세요.

    # # 누적한 iterator에서 중복에 상관 없이 순서에 상관 있게 3개씩 출력하세요.
    # z = itertools.permutations([1, 2, 3], 2)
    # print(list(z))
    x = itertools.repeat(3, 3)
    x = itertools.accumulate(x)
    x = itertools.permutations(x, 3)

    for i in x:
        print(i)


if __name__ == "__main__":
    main()

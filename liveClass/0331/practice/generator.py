# 0부터 매개변수로 주어진 숫자만큼 iterator를 생성하는 generator 함수를 정의하세요.


def main():
    # 정의한 generator를 가지고 iterator를 정의하고, 멤버를 꺼내서 출력하세요.
    def gen():
        yield 0
        yield 1
        yield 2
        yield 3

    generator = gen()
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))


if __name__ == "__main__":
    main()

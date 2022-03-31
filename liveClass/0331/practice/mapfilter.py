from tkinter.tix import Tree


def main():

    numbers = [1, 2, 3, 4, 5, 6]

    # 아래의 코드를 완성하세요.
    # map(함수, iterable)
    numbers_squared = list(map(lambda x: x**2, numbers))
    print(numbers_squared)

    # filter(함수, iterable)
    # 아래의 코드를 완성하세요.
    numbers_even = list(filter(lambda x: True if x %
                        2 == 0 else False, numbers))
    print(numbers_even)


if __name__ == "__main__":
    main()

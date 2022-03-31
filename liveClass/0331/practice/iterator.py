

def main():
    elice = ['e', 'l', 'i', 'c', 'e']

    # next() 혹은 반복문을 이용해 요소를 꺼내세요.
    elice_iter = iter(elice)
    print(next(elice_iter))
    print(next(elice_iter))
    print(next(elice_iter))
    print(next(elice_iter))
    print(next(elice_iter))


if __name__ == "__main__":
    main()

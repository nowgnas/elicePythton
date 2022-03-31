def main():
    first_name = ['elice', 'mad', 'cheshire', 'dodo', 'heart']
    last_name = ['rabbit', 'hatter', 'cat', 'bird', 'queen']

    # first_name을 첫 번째 요소, last_name을 두 번째 요소로 가지는 튜플을 출력하세요.
    for first, last in zip(first_name, last_name):
        print((first, last))


if __name__ == "__main__":
    main()

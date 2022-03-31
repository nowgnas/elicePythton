def main():
    hi_elice = ['Hi', 'Bye', 'I\'m', 'elice', 'rabbit']

    # 위의 리스트를 iterator로 변환한 뒤, 언패킹하세요.
    iterator = iter(hi_elice)

    # 언패킹 결과에서 출력 결과에 해당하는 변수만 출력하세요.
    a, b, c, d, e = iterator
    print(a, c, d)


if __name__ == "__main__":
    main()

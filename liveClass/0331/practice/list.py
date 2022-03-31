def main():

    msg = "I_love_python"

    # 아래의 코드를 완성하세요.
    lst = msg.split('_')

    word_len_list = [len(x) for x in lst]
    print(word_len_list)

    # > dict도 list comprehention이 된다
    d = {key: value for key, value in zip(range(5), range(5))}
    print(d)


if __name__ == "__main__":
    main()

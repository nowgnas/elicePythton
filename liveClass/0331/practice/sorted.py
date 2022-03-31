def main():
    # attendance = ['Elice Rabbit', 'Mad Hatter',
    #               'Cheshire Cat', 'Dodo Bird', 'Heart Queen']

    # # 출석부를 오름차순으로 정렬하여 출력하세요.
    # print(sorted(attendance))
    student_tuples = [('jane', 'C', 12), ('dave', 'B', 10), ('john', 'A', 15)]
    print(sorted(student_tuples, key=lambda x: x[1]))


if __name__ == "__main__":
    main()

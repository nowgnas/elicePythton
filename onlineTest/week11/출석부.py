# 지시사항을 참고하여 코드를 작성하세요.
def filter_num(student):
    students = sorted(student.items(), key=lambda x: x[0])
    answer = []
    for key, _ in students:
        answer.append(key)

    return answer


# 값을 확인하기 위한 코드입니다. 값을 변경해가며 테스트해 보세요!
student = {
    1: "엘리스 토끼",
    3: "모자장수",
    6: "캐터필러",
    5: "하트여왕",
    2: "도도새",
    9: "신발장수",
    7: "모자 쓴 행인",
}
print(filter_num(student))

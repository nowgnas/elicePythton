# 지시사항을 참고하여 코드를 작성하세요.
def check_log(log_1p, log_2p):
    answer = ''
    for _1p, _2p in zip(log_1p, log_2p):
        if '회피' in _1p:
            answer = '1p'
            break
        if '회피' in _2p:
            answer = '2p'
            break
    return answer


# 값을 확인하기 위한 코드입니다. 값을 변경해가며 테스트해 보세요!
print(check_log(["@회복~", "!공격!", "!공격!", "!공격!", "!공격!"],
      ["@회복~#", "!공격!", "!공격!", "@회복~", "#회피"]))


def scoring():
    import main as submission

    d00 = submission.NOR(0, 0)
    d01 = submission.NOR(0, 1)
    d10 = submission.NOR(1, 0)
    d11 = submission.NOR(1, 1)

    print("입력 = [(0,0), (0,1), (1,0), (1,1)]")    # 1 0 0 0
    print("정답 = [  1,     0,     0,     0]")    # 1 0 0 0
    print("결과 = {:4}{:7}{:7}{:7}\n".format(d00, d01, d10, d11))

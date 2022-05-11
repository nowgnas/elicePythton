import numpy as np
import matplotlib.pyplot as plt


# TODO : weight 와 bias 값을 설정.
# XOR 문제를 풀기 위한 W 와 B 값
# W1 의 3 행과 W2 의 2, 3 행은 수정하지 않는다.
W1 = [[-1.0, -0.5, 1.1],
      [0.7, 1.4, -0.5],
      [0, 0, 1]]
W2 = [[0.4, 0.4, -0.7],
      [0, 0, 0],
      [0, 0, 0]]


def main():

    # (0,0), (0,1), (1,0), (1,1) 을 입력으로 처리.
    Ex00 = [0, 0, 1]
    Ex01 = [0, 1, 1]
    Ex10 = [1, 0, 1]
    Ex11 = [1, 1, 1]

    # XOR 값 확인
    print("x1, x2 = (0, 0) : ", DLP_XOR(Ex00, W1, W2))
    print("x1, x2 = (0, 1) : ", DLP_XOR(Ex01, W1, W2))
    print("x1, x2 = (1, 0) : ", DLP_XOR(Ex10, W1, W2))
    print("x1, x2 = (1, 1) : ", DLP_XOR(Ex11, W1, W2))

    # x1, x2 각각 -0.5 에서 1.5 까지 0.1 간격 표시, XOR 결과 저장
    result = []

    for i in range(-5, 15, 1):
        for j in range(-5, 15, 1):
            result.append([i/10.0, j/10.0,
                           DLP_XOR([i/10.0, j/10.0, 1], W1, W2)])

    # XOR 시각화
    # result 의 x,y, color 을 분리
    x = [i[0] for i in result]
    y = [i[1] for i in result]
    z = [i[2] for i in result]

    fig, ax = plt.subplots(figsize=(8, 8))

    ax.scatter(x, y, c=z, alpha=0.5)
    ax.scatter([0, 1], [1, 0], s=200, c='green', alpha=0.5)
    ax.scatter([0, 1], [0, 1], s=200, c='red', alpha=0.5)

    # W1 에 담긴 값의 의미
    if (W1[0][1] < 0.0001 and W1[0][1] > -0.0001):
        W1[0][1] = 0.001
    if (W1[1][1] < 0.0001 and W1[1][1] > -0.0001):
        W1[1][1] = 0.001
    x_1 = np.array(range(-5, 15, 1))/10.0
    y_1 = -W1[0][0]/W1[0][1]*x_1 - W1[0][2]/W1[0][1]
    x_2 = np.array(range(-5, 15, 1))/10.0
    y_2 = -W1[1][0]/W1[1][1]*x_1 - W1[1][2]/W1[1][1]

    ax.plot(x_1, y_1, x_2, y_2)
    ax.set_xlim([-0.5, 1.5])
    ax.set_ylim([-0.5, 1.5])

    ax.set_xlabel('X1')
    ax.set_ylabel('X2')

    fig.savefig("plot.png")


def DLP_XOR(X, W1, W2):
    # 입력
    x = np.array(X)

    # 가중치와 편차(W,B) 입력
    w1 = np.array(W1)
    w2 = np.array(W2)

    # 연산
    h1 = np.array([0.0]*len(X))
    y = np.array([0]*len(X))

    for count in range(len(X)):
        h1[count] = np.sum(x*w1[count]) > 0
    for count in range(len(x)):
        y[count] = np.sum(h1*w2[count]) > 0
    return y[0]


if __name__ == "__main__":
    main()

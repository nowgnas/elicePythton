import numpy as np
# 1. 가중치와 Bias 값을
#    임의로 설정해줍니다.

#    Step01. 0이상 1미만의 임의의 값으로 정의된
#            4개의 가중치 값이 들어가있는
#            1차원 리스트를 정의해줍니다.
weight = np.array([0.5, 0.5, 0.3, 0.3])

#    Step02. Bias 값을 임의의 값으로 설정해줍니다.
bias = 0.7

# 2. 신호의 총합과 그에 따른 결과 0 또는 1을
#    반환하는 함수 perceptron을 완성합니다.


def perceptron(x, w, b):
    sum_out = 0
    for _x, _w in zip(x, w):
        sum_out += _x*_w
    y = 1 if sum_out+b >= 0 else 0
    return sum_out, y


#    Step01. 입력 받은 값과 Bias 값을 이용하여
#            신호의 총합을 구합니다.

#    Step02. 신호의 총합이 0 이상이면 1을,
#            그렇지 않으면 0을 반환하는 활성화
#            함수를 작성합니다.


# 입력 값 리스트, 가중치 리스트, bias를 매개변수로 받는 퍼셉트론을 만들어보세요.
# 퍼셉트론은 입력된 매개변수를 계산한 결과에 따라 (출력값, 활성화 함수)를 반환합니다.
def main():

    x = [1, 2, 3, 4]

    w = [0.3, 0.5, 0.1, 0.7]
    b = -2

    output, y = perceptron(w, x, b)

    print('output: ', output)
    print('y: ', y)

if __name__ == '__main__':
    main()
    
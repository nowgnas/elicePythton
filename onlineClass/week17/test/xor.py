import numpy as np
import tensorflow as tf


def main():
    # XOR 문제를 위한 데이터 생성
    training_data = np.array(
        [[0, 0],
         [0, 1],
         [1, 0],
         [1, 1]], "float32")
    target_data = np.array(
        [[0],
         [1],
         [1],
         [0]], "float32")

    '''
    1. 다층 퍼셉트론 모델을 생성합니다.
    2. 모델의 손실 함수, 최적화 방법, 평가 방법을 설정합니다.
    3. 모델을 학습시킵니다. epochs를 자유롭게 설정해보세요.
    '''
    # 1. 모델 생성
    model = tf.keras.Sequential()
    model.add(
        tf.keras.layers.Dense(
            16,
            input_dim=2,
            activation='relu'
        )
    )
    model.add(
        tf.keras.layers.Dense(
            1,
            activation='sigmoid'
        )
    )
    # 평가 점수를 확인하고 싶다면
    # `모델 학습 결과.history['binary_accuracy'][-1]`을 출력해보세요.

    model.compile(
        loss='mse',
        optimizer='adam',
        metrics=['binary_accuracy']
    )

    # 3. 모델 학습
    hist = model.fit(
        x=training_data,
        y=target_data,
        epochs=100
    )
    print(hist.history['binary_accuracy'][-1])

    # 4. 채점
    return hist


if __name__ == "__main__":
    main()

import tensorflow as tf
from tensorflow import keras


def make_model1():
    # TODO: 첫번째 모델의 그림대로 만들어주세요.
    model1 = keras.models.Sequential([
        keras.layers.Dense(units=100, input_dim=2),
        keras.layers.Dense(300, activation='relu'),
        keras.layers.Dense(50, activation='relu'),
        keras.layers.Dense(10, activation='softmax')
    ])

    return model1


def make_model2():
    # TODO: 두번째 모델의 그림대로 만들어주세요.
    model2 = keras.models.Sequential([
        keras.layers.Dense(units=20, input_dim=100),
        keras.layers.Dense(128, activation='relu'),
        keras.layers.Dense(256, activation='relu'),
        keras.layers.Dense(10, activation='softmax')
    ])

    return model2


def make_model3():
    # TODO: 세번째 모델의 그림대로 만들어주세요.
    model3 = keras.models.Sequential([
        keras.layers.Dense(100, input_dim=10),
        keras.layers.Dense(256, activation='sigmoid'),
        keras.layers.Dense(32, activation='relu'),
        keras.layers.Dense(10, activation='softmax')
    ])

    return model3


def main():
    model1 = make_model1()
    model2 = make_model2()
    model3 = make_model3()


if __name__ == "__main__":
    main()

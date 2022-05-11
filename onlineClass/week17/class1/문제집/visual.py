from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
mpl.use("Agg")


def Visualize():
    digits = load_digits()
    ndarray = digits.images[-5]
    plt.figure(1)
    plt.imshow(ndarray, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.show()

    plt.savefig("plot.png")
    print('예시 이미지: ')

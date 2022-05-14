import numpy as np
import matplotlib.pyplot as plt

from elice_utils import EliceUtils
elice_utils = EliceUtils()


def Visual(activations_1):
    plt.figure(1)
    for i, a in activations_1.items():
        plt.subplot(1, len(activations_1), i+1)
        plt.title(str(i+1) + '-layer')
        plt.hist(a.flatten(), 30, range=(0, 1))
    plt.show()

    plt.savefig("plot1.png")
    elice_utils.send_image("plot1.png")

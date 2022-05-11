import matplotlib.pyplot as plt
import seaborn as sns


def data_plot(x1, x2):

    fig, ax = plt.subplots()

    ax.scatter(x1['sepal_length'], x1['petal_length'])
    ax.scatter(x2['sepal_length'], x2['petal_length'])
    ax.set_xlabel('Sepal Length')
    ax.set_ylabel('Petal Length')
    fig.savefig("iris_plot.png")


def sub_plot(x, y, z, x1, x2, lx, ly, rx, ry):

    fig, ax = plt.subplots()

    # 산점도
    ax.scatter(x, y, c=z, alpha=0.1)
    ax.scatter(x1['sepal_length'], x1['petal_length'])
    ax.scatter(x2['sepal_length'], x2['petal_length'])

    # 직선
    ax.plot([lx, rx], [ly, ry])

    ax.set_xlabel('Sepal Length')
    ax.set_ylabel('Petal Length')

    fig.savefig("result_plot.png")

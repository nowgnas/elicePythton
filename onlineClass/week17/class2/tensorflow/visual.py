import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D

# from elice_utils import EliceUtils
# elice_utils = EliceUtils()


def Visualize(x_data, y_data, predictions):
    # 데이터 출력
    plt.scatter(x_data, y_data)
    plt.savefig('onlineClass/week17/class2/tensorflow/data.png')
    # elice_utils.send_image('data.png')

    # 곡선형 분포 데이터와 예측값 출력
    plt.scatter(x_data, predictions, color='red')
    plt.savefig('onlineClass/week17/class2/tensorflow/prediction.png')
    # elice_utils.send_image('prediction.png')

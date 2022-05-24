import sys
import numpy
import cv2
from elice_utils import EliceUtils

elice_utils = EliceUtils()


def binarization(img, threshold):
    # img를 이진이미지로 만든 뒤, 이진 이미지를 반환하는 함수를 구현하세요.
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img[i, j] = 255 if img[i, j] >= threshold else 0

    return img


if __name__ == "__main__":
    threshold = int(sys.argv[1])
    img = cv2.imread("elice.jpg", cv2.IMREAD_GRAYSCALE)

    binary_img = binarization(img, threshold)

    cv2.imwrite("result.jpg", binary_img)
    elice_utils.send_image('result.jpg')

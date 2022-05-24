import sys
import cv2
import numpy

from elice_utils import EliceUtils
elice_utils = EliceUtils()


# 영상을 입력으로 받아 영상의 히스토그램 영상을 리턴하는 함수를 만드세요.
def draw_histogram(img):
    total_pixel = img.shape[0] * img.shape[1]
    histogram_img = numpy.ones((total_pixel, 256)) * 255
    histogram = [0 for i in range(256)]

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            histogram[img[i, j]] += 1
    for intensity, freqency in enumerate(histogram):
        start = (intensity, total_pixel - 1)
        end = (intensity, total_pixel - freqency - 1)
        cv2.line(histogram_img, start, end, (0), 2, cv2.LINE_AA)

    return histogram_img


if __name__ == "__main__":
    # 이미지를 읽어옵니다.
    img = cv2.imread("./night.jpg", cv2.IMREAD_GRAYSCALE)

    # 결과를 확인합니다.
    histogram_img = draw_histogram(img)
    histogram_img = cv2.resize(histogram_img, (256, 256))

    cv2.imwrite('result.jpg', histogram_img)
    elice_utils.send_image('result.jpg')

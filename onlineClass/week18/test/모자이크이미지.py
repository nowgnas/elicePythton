from elice_utils import EliceUtils

elice_utils = EliceUtils()

from PIL import Image


# 이미지를 불러옵니다.
def main():
    elice_image = Image.open("elice.png")
    print('=' * 25, "원본", '=' * 25)

    elice_utils.send_image("elice.png")

    # 불러온 이미지의 사이즈를 확인합니다.
    print("이미지 크기:", elice_image.size)
    print()

    # 모자이크(정사각형)의 크기를 설정합니다.
    m_size = 8

    # 정사각형을 하나씩 순회합니다.
    for i1 in range(0, elice_image.size[0], m_size):
        for j1 in range(0, elice_image.size[1], m_size):
            r_sum = 0
            g_sum = 0
            b_sum = 0

            # 정사각형 범위 내 각 픽셀의 RGB 값을 추출하여 평균을 냅니다.
            for i2 in range(i1, i1 + m_size):
                for j2 in range(j1, j1 + m_size):
                    # (i2, j2) 픽셀의 값을 불러옵니다.
                    rgb = elice_image.getpixel((i2, j2))

                    # TODO:[지시사항 1번]  RGB 채널별로 픽셀 값을 구하여 더합니다.
                    r_sum += rgb[0]
                    g_sum += rgb[1]
                    b_sum += rgb[2]

            # TODO: [지시사항 2번] RGB 채널별로 현재 정사각형 영역 내 픽셀값의 평균을 구합니다.
            r_avg = round(r_sum / (m_size * m_size))
            g_avg = round(g_sum / (m_size * m_size))
            b_avg = round(b_sum / (m_size * m_size))

            # 구한 평균값을 현재 정사각형의 모든 픽셀에 적용합니다.
            for i2 in range(i1, i1 + m_size):
                for j2 in range(j1, j1 + m_size):
                    elice_image.putpixel((i2, j2), (r_avg, g_avg, b_avg))  # putpixel 함수 사용

    elice_image.save("elice_mozaic.png")
    print('=' * 25, "모자이크", '=' * 25)
    elice_utils.send_image("elice_mozaic.png")


if __name__ == '__main__':
    main()
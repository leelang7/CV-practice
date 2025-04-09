import sys
import numpy
import cv2


def convolution2D(img, kernel):
    dst = img.copy()
    # 주어진 커널을 입력 img에 회선처리한 이미지 dst를 반환하는 함수를 완성하세요.
    center_r = kernel.shape[0] // 2
    center_c = kernel.shape[1] // 2
    
    for i in range(center_r, img.shape[0] - center_r):
        for j in range(center_c, img.shape[1] - center_c):
            intensity = 0
            for r in range(kernel.shape[0]):
                for c in range(kernel.shape[1]) :
                    x = + i + r - center_r
                    y = + j + c - center_c
                    intensity += img[x, y] * kernel[r, c]
            dst[i, j] = intensity
    return dst


def prewitt(img):
    vertical_kernel = numpy.array(
        [
            [ -1, 0, 1],
            [ -1, 0, 1],
            [-1, 0, 1]
        ]
    )
    
    horizontal_kernel = numpy.array(
        [
            [ -1, -1, -1],
            [ 0, 0, 0],
            [1, 1, 1]
        ]
    )

    # 프리윗 필터에 회선처리를 적용합니다.
    dst_vertical_edge = convolution2D(img, vertical_kernel)
    dst_horizontal_edge = convolution2D(img, horizontal_kernel)
    
    return dst_vertical_edge + dst_horizontal_edge


if __name__ == "__main__":
    # 이미지를 불러옵니다.
    img = cv2.imread("elice2.png", cv2.IMREAD_GRAYSCALE)
    
    # 회선처리 함수를 적용한 프리윗 필터를 적용해봅니다.
    filtered_img = prewitt(img)
    cv2.imwrite("processing_result.jpg", filtered_img)    
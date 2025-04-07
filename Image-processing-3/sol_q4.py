import sys
import numpy
import cv2


# thredshold를 기준으로 img를 이진 이미지로 만든 뒤 반환하는 함수를 구현하세요.
def binarization(img, threshold):
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img[i, j] = 255 if img[i, j] >= threshold else 0

    return img


if __name__ == "__main__":
    # 임계값 128이 주어집니다.
    threshold = int(sys.argv[1])
    
    # 이미지를 불러옵니다.
    img = cv2.imread("elice.jpg", cv2.IMREAD_GRAYSCALE)
    
    # 이진화 결과를 확인합니다.
    binary_img = binarization(img, threshold)
    
    cv2.imwrite("result.jpg", binary_img)
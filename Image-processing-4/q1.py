import numpy as np


def intersection_over_union(box1, box2):
    iou = 0
    # 교집합 부분의 top left 좌표와 bottom right 좌표를 계산하세요.
    
    
    # 교집합의 넒이를 구하세요.
    
    
    # 박스1의 넓이와 박스2의 넓이를 각각 구하세요.
    
    
    # 두 박스의 넒이를 더한뒤 교집합 영역 넓이를 뺴 합영역을 구하세요.
    
    
    # 교집합의 넓이와 합영역을 이용해 IoU를 계산 후 반환하세요.
    
    
    return iou


if __name__ == "__main__":
    # 아래 두 박스는 좌상단 모서리 점과 우하단 모서점으로 표현됩니다. 
    box1 = [100, 100, 170, 180]
    box2 = [130, 140, 250, 300]
    
    # 완성한 함수를 호출하여 소수점 다섯째 자리에서 반올림하여 값을 출력합니다.
    iou = intersection_over_union(box1, box2)
    print(round(iou, 5))

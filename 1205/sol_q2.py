import numpy
from sklearn.metrics import auc, average_precision_score
from matplotlib import pyplot as plt


# average precision을 반환하는 함수를 완성하세요.
def average_precision(detection_results, ground_truth):
    precisions, recalls = [], []
    for i in range(detection_results.shape[0]): # 10
        threshold = detection_results[i, 1]

        detected = detection_results[numpy.where(detection_results[:, 1] >= threshold)]
        TP = detected[numpy.where(detected[:, 0] == 1)]
        precision = TP.shape[0] / detected.shape[0]
        recall = TP.shape[0] / ground_truth

        print(f"precision = {TP.shape[0]}/{detected.shape[0]}, recall = {TP.shape[0]}/{ground_truth}")
        precisions.append(precision)
        recalls.append(recall)

    ap = auc(recalls, precisions);
    # matplotlib로 커브 곡선을 눈으로 확인해봅시다.
    print(f"Area under curve = {ap}")
    plt.plot(recalls, precisions, marker='.')
    plt.savefig('precision-recall.png', dpi=300)
    return ap


def main():
    detection_results = numpy.array([
        [1, 0.95],
        [1, 0.91],
        [1, 0.85],
        [1, 0.81],
        [1, 0.78],
        [0, 0.68],
        [1, 0.57],
        [1, 0.45],
        [0, 0.43],
        [0, 0.13],
    ])
    
    # 정의한 함수를 호출한 결과를 소수점 다섯째 자리에서 반올림하여 확인합니다.
    ap = average_precision(detection_results, 15)
    print(round(ap, 4))


if __name__ == "__main__":
    main()
import sys
import cv2


def relocate_img_pieces(img, from_idx, to_idx):
    half_row = img.shape[0] // 2
    half_col = img.shape[1] // 2
    
    start_pt1, start_pt2 \
        = tuple(map(lambda x: x * half_row, divmod(from_idx, 2))), tuple(map(lambda y: y * half_col, divmod(to_idx, 2)))

    tmp = img[start_pt1[0]: start_pt1[0] + half_row, start_pt1[1]: start_pt1[1] + half_col].copy()

    img[start_pt1[0]: start_pt1[0] + half_row, start_pt1[1]: start_pt1[1] + half_col]  \
        = img[start_pt2[0]: start_pt2[0] + half_row, start_pt2[1]: start_pt2[1] + half_col]
        
    img[start_pt2[0]: start_pt2[0] + half_row, start_pt2[1]: start_pt2[1] + half_col]  \
        = tmp[:]

    return img

# 주어진 영상과 조각 순서를 보고 원본 영상(출력 예시 참고)으로 복원한 영상을 반환하는 함수를 구현하세요.
def solve_puzzle(img, place_order):
    for to_idx, from_idx in enumerate(piece_order):
        if to_idx == from_idx:
            continue
        
        proper_piece_idx = piece_order.index(to_idx)
        piece_order[to_idx], piece_order[proper_piece_idx] = piece_order[proper_piece_idx], from_idx
        img = relocate_img_pieces(img, to_idx, proper_piece_idx)
    
    return img
    

# python {파일명} 3,2,1,0
if __name__ == "__main__":
    # 퍼즐의 순서가 리스트 형태로 입력됩니다.
    piece_order = list(map(int, list(sys.argv[1].split(','))))
    print(piece_order)
    
    # 이미지를 불러옵니다.
    img = cv2.imread("./puzzle.jpg", cv2.IMREAD_GRAYSCALE)
    
    # 복원 결과를 확인합니다.
    result_img = solve_puzzle(img, piece_order)
    cv2.imwrite('puzzle_result.jpg', result_img) 
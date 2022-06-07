import glob

import cv2
import numpy as np


file_list = glob.glob('.\\img\\*.jpg')
img_name_list = []
count = 0
for i in file_list:
    print(i)
    img_name_list.append(i[6:])
    img = cv2.imread(i)
    print(img.shape)
    rows, cols = img.shape[:2]


    # 어핀 변환 부분
    # pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
    # pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
    # # pts1와 pts2 좌표점을 이용해서 전체적으로 이미지 비틀기
    # M = cv2.getAffineTransform(pts1, pts2)
    # dst = cv2.warpAffine(img, M, (cols, rows))

    exp = 2              # 볼록, 오목 지수 (오목 : 0.1 ~ 1, 볼록 : 1.1~)
    scale = 1            # 변환 영역 크기 (0 ~ 1)

    # 매핑 배열 생성
    mapy, mapx = np.indices((rows, cols),dtype=np.float32)

    # 좌상단 기준좌표에서 -1~1로 정규화된 중심점 기준 좌표로 변경
    mapx = 2*mapx/(cols-1)-1
    mapy = 2*mapy/(rows-1)-1

    # 직교좌표를 극 좌표로 변환
    r, theta = cv2.cartToPolar(mapx, mapy)

    # 왜곡 영역만 중심확대/축소 지수 적용
    r[r< scale] = r[r<scale] ** exp

    # 극 좌표를 직교좌표로 변환
    mapx, mapy = cv2.polarToCart(r, theta)

    # 중심점 기준에서 좌상단 기준으로 변경
    mapx = ((mapx + 1)*cols-1)/2
    mapy = ((mapy + 1)*rows-1)/2
    # 재매핑 변환
    distorted = cv2.remap(img,mapx,mapy,cv2.INTER_LINEAR)

    # cv2.imshow('origin', img)
    cv2.imshow('distorted', distorted)
    cv2.imwrite('./lens_img/lens_{0}'.format(img_name_list[count]), distorted)
    cv2.waitKey()
    cv2.destroyAllWindows()
    count += 1


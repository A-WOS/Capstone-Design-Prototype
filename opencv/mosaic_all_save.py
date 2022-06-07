import glob

import cv2


def mosaic(img, ratio=0.1):
    small = cv2.resize(img, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    return cv2.resize(small, img.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)


# 좀 안됨
file_list = glob.glob('.\\img\\*.jpg')
img_name_list = []
count = 0
for i in file_list:
    print(i)
    img_name_list.append(i[6:])
    img = cv2.imread(i)
# img = cv2.imread('./img/elephant.jpg')                     # 이미지 읽기

    result1 = mosaic(img)
    # cv2.imshow('result1', result1)

    result2 = mosaic(img, ratio=0.05)
    # cv2.imshow('result2', result2)  # 채택
    cv2.imwrite('./mosaic_img/mosaic_{0}'.format(img_name_list[count]), result2)
    cv2.waitKey()
    cv2.destroyAllWindows()
    count += 1

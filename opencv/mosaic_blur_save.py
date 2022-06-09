import glob

import cv2

file_list = glob.glob('.\\img\\*.jpg')
img_name_list = []
count = 0
for i in file_list:
    print(i)
    img_name_list.append(i[6:])
    img = cv2.imread(i)
    ksize = 60                                              # 블러 처리에 사용할 커널 크기
    win_title = 'mosaic'                                    # 창 제목
    # img = cv2.imread('./img/elephant.jpg')                     # 이미지 읽기

    roi = cv2.blur(img, (ksize, ksize))             # 블러(모자이크) 처리
    # cv2.imshow(win_title, roi)
    cv2.imwrite('./blur_img/blur_{0}'.format(img_name_list[count]), roi)
    cv2.waitKey()
    cv2.destroyAllWindows()
    count += 1

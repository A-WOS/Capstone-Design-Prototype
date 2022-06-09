import glob
import random
import cv2
import numpy as np


file_list = glob.glob('.\\img\\*.jpg')
img_name_list = []
count_jdg = 0
for i in file_list:
    print(i)
    img_name_list.append(i[6:])
    img = cv2.imread(i)
# img = cv2.blur(img, (20, 20))
    for j in range(9):
        globals()['org_{0}'.format(j)] = img.copy()
    print(img.shape)
    row, col = img.shape[:2]
    row_list = [row/3, row*2/3, row]
    col_list = [col/3, col*2/3, col]
    row_list = list(map(int, row_list))
    col_list = list(map(int, col_list))
    img_list = []
    first_col = 0
    count = 0

    for col in row_list:
        first_row = 0
        for row in col_list:
            img_list.append(globals()['org_{0}'.format(count)][first_col:col, first_row:row])
            first_row = row
        first_col = col
        count += 1

    avg_row = int(row/3)
    avg_col = int(col/3)
    print(len(img_list))
    resize_img_list = []
    for x in img_list:
        # 이미지 출력 부분 주석
        # cv2.imshow("a".format(x), x)
        resize_img_list.append(cv2.resize(x, (avg_row, avg_col)))
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # 내 공부용
    # axis = 0 -- 가로 || axis = 1 -- 세로
    # cv2.vconcat([img,img2]) -- 가로 || cv2.hconcat([img,img2]) -- 세로
    
    # 랜덤으로 순서 섞기
    random.shuffle(resize_img_list)
    # for i in img_list:
    #     cv2.imshow("a".format(i), i)
    #     cv2.waitKey(0)
    #     cv2.destroyAllWindows()

    test_img_list = []
    for k in [0, 3, 6]:
        x = resize_img_list[k+0]
        y = resize_img_list[k+1]
        z = resize_img_list[k+2]
        test_img_list.append(cv2.hconcat([x, y, z]))

    test_img = cv2.vconcat([test_img_list[0], test_img_list[1], test_img_list[2]])
    
    # 이미지 출력할 필요가 없다..
    # cv2.imshow("test", test_img)
    cv2.imwrite('./random_img/random_{0}'.format(img_name_list[count_jdg]), test_img)
    cv2.waitKey(0)
    count_jdg += 1

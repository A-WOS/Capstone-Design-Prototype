
import glob
import random
import cv2
import numpy as np


img = cv2.imread("img/elephant.jpg")
for i in range(9):
    globals()['org_{0}'.format(i)] = img.copy()
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

print(len(img_list))
for i in img_list:
    cv2.imshow("a".format(i), i)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# axis = 0 -- 가로 || axis = 1 -- 세로
# cv2.vconcat([img,img2]) -- 가로 || cv2.hconcat([img,img2]) -- 세로
test_img_list = ["test_img1", "test_img2", "test_img3"]
rand_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(rand_list)
for i in test_img_list:
    x = rand_list.pop(0)
    y = rand_list.pop(0)
    z = rand_list.pop(0)
    test_img = np.concatenate([img_list[x], img_list[y]], axis=0)

    # i = np.concatenate([img_list[x][0:(int(col/3)-2), 0:(int(row/3)-2)],
    #                     img_list[y][0:(int(col/3)-2), 0:(int(row/3)-2)],
    #                     img_list[z][0:(int(col/3)-2), 0:(int(row/3)-2)]], axis=1)
    # # i = cv2.vconcat(img_list[x][0:int(col/3)-2, 0:int(row/3)],
    # #                 img_list[y][0:int(col/3)-2, 0:int(row/3)])
    # # i = cv2.vconcat(i, img_list[z][int(col / 3) - 2, int(row / 3) - 2])
# test_img = np.concatenate([test_img_list[0], test_img_list[1], test_img_list[2]], axis=1)
test_img = test_img_list[0]
cv2.imshow("test", test_img_list[0])
cv2.waitKey(0)


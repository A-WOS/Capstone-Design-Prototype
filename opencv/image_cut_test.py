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
i = int(random.randint(0, 8))
j = int(random.randint(0, 8))
test_img = np.concatenate([img_list[i], img_list[j]], axis=1)
cv2.imshow("test", test_img)
cv2.waitKey(0)


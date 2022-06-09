import glob

import cv2


file_list = glob.glob('.\\img\\*.jpg')
img_name_list = []
count = 0
for i in file_list:
    print(i)
    img_name_list.append(i[6:])
    gray_img = cv2.imread(i, cv2.IMREAD_GRAYSCALE)
    # gray_img = cv2.imread('./img/elephant.jpg', cv2.IMREAD_GRAYSCALE)

    # threshold 값에 따라 결과 달라짐 - 클수록 긴 선만 나옴
    threshold1 = 200
    threshold2 = 200
    edge_img = cv2.Canny(gray_img, threshold1, threshold2)
    # cv2.imwrite('sample_edge.jpg', edge_img)
    # cv2.imshow("edge_img", edge_img)
    cv2.imwrite('./canny_img/canny_{0}'.format(img_name_list[count]), edge_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    count += 1

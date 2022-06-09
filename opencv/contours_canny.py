import cv2

gray_img = cv2.imread('./img/elephant.jpg', cv2.IMREAD_GRAYSCALE)

# threshold 값에 따라 결과 달라짐 - 클수록 긴 선만 나옴
threshold1 = 200
threshold2 = 200
edge_img = cv2.Canny(gray_img, threshold1, threshold2)
# cv2.imwrite('sample_edge.jpg', edge_img)
cv2.imshow("edge_img", edge_img)
cv2.waitKey(0)

cv2.destroyAllWindows()

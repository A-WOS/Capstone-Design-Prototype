import cv2
import numpy as np

img = cv2.imread("./img/elephant.jpg", cv2.IMREAD_COLOR)
h, w, c = img.shape
black = np.zeros((h, w, c), np.uint8)
white = np.zeros((h, w, c), np.uint8)
white.fill(255)

# color -> gray
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
binary = cv2.bitwise_not(binary)
# 이진화

# RETR_EXTERNAL 최와곽 라인만 찾음
contours, hierachy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# 외곽선 그리기
cv2.drawContours(black, contours, -1, (0, 0, 255), 2)
cv2.drawContours(white, contours, -1, (0, 0, 255), 2)
# 원본 + 외곽선 
cv2.imshow("img", img)
# 흑백
cv2.imshow("gray", gray)
# 검정부분
cv2.imshow("black", black)
cv2.imshow("white", white)
cv2.waitKey(0)

cv2.destroyAllWindows()

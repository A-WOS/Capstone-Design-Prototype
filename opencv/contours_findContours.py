import cv2
import numpy as np

img = cv2.imread("./img/cat.jpg", cv2.IMREAD_COLOR)
h, w, c = img.shape
black = np.zeros((h, w, c), np.uint8)
white = np.zeros((h, w, c), np.uint8)
white.fill(255)

# color -> gray
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
ret, binary = cv2.threshold(gray, 210, 255, cv2.THRESH_BINARY)
binary = cv2.bitwise_not(binary)
# 이진화

# RETR_EXTERNAL 최와곽 라인만 찾음
contours, hierachy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

contours_data = np.array(contours)
contours_data.shape

value = list()
for i in range(len(contours_data)):
    for j in range(len(contours_data[i])):
        value.append(contours_data[i][j][0][0])  # 네번째 괄호가 0일때 x의 값
        x_min = min(value)
        x_max = max(value)
print(x_min)
print(x_max)

# y의 min과 max 찾기
y_min, y_max = 0, 0
value = list()
for i in range(len(contours_data)):
    for j in range(len(contours_data[i])):
        value.append(contours_data[i][j][0][1])  # 네번째 괄호가 0일때 x의 값
        y_min = min(value)
        y_max = max(value)
print(y_min)
print(y_max)
data_field = img[y_min:y_min+y_max, x_min:x_min+x_max]

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
cv2.imshow("binary", 255-binary)

# 원하는 부분만 잘라보려 했는데 외곽선 부분만 자르는건 안되더라
# contours를 담는 최소 크기의 사각형 필드
cv2.imshow("data_field", data_field)
cv2.waitKey(0)

cv2.destroyAllWindows()

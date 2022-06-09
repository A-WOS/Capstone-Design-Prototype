import cv2

# 그냥 blur 함수만 써도 될듯?
for i in [20, 40, 60, 80, 100]:
    ksize = i                                              # 블러 처리에 사용할 커널 크기
    win_title = 'mosaic'                                    # 창 제목
    img = cv2.imread('./img/elephant.jpg')                     # 이미지 읽기

    roi = cv2.blur(img, (ksize, ksize))             # 블러(모자이크) 처리
    cv2.imshow(win_title, roi)
    cv2.waitKey(0)

    cv2.destroyAllWindows()

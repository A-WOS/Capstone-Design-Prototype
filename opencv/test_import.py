import cv2


# 테스트용

def test_import(img):
    img = cv2.imread(img)                     # 이미지 읽기


    def mosaic(image, ratio=0.1):
        small = cv2.resize(image, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
        return cv2.resize(small, img.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)


    result1 = mosaic(img)
    cv2.imshow('result1', result1)

    result2 = mosaic(img, ratio=0.05)
    # cv2.imshow('result2', result2)  # 채택
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return result2

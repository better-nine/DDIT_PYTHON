import cv2
import numpy as np
 
# 이미지 읽기
#img = cv2.imread('lena.jpg', cv2.IMREAD_REDUCED_COLOR_4) 
img = cv2.imread('lena.jpg', 2) 
 
re_img = cv2.resize(img, dsize=(100, 100), interpolation=cv2.INTER_AREA) 
 
cv2.imshow('Test Image', re_img)
cv2.waitKey(0)

# 이미지 윈도우 삭제
cv2.destroyAllWindows()

# 이미지 다른 파일로 저장
#cv2.imwrite('test.png', img)
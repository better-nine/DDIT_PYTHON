import cv2
import numpy as np
 
# 이미지 읽기
img = cv2.imread('lena.jpg', cv2.COLOR_BGR2GRAY)

img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
# 이미지 화면에 표시
cv2.imshow('Test Image', img_g)
cv2.waitKey(0)

# 이미지 윈도우 삭제
cv2.destroyAllWindows()
 
# 이미지 다른 파일로 저장
#cv2.imwrite('test.png', img)
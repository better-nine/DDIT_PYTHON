import cv2
import numpy as np
 

img = cv2.imread('lena.jpg', 1) 
 

img90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

   
cv2.imshow('Test Image', img90)
cv2.waitKey(0)

# 이미지 윈도우 삭제
cv2.destroyAllWindows()

# 이미지 다른 파일로 저장
#cv2.imwrite('test.png', img)
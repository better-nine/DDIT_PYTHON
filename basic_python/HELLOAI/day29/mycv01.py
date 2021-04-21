import cv2
import numpy as np
 
# 이미지 읽기
img = cv2.imread('3_4.png', 1)

img[0][0][0] = 255
img[0][0][1] = 255
img[0][0][2] = 255
print(img)
print(len(img))

for i in img:
    for j in i:
        j[0] = 0
        j[1] = 0
        j[2] = 255
        print(j)
 
 
# 이미지 화면에 표시
cv2.imshow('Test Image', img)
cv2.waitKey(0)

# 이미지 윈도우 삭제
cv2.destroyAllWindows()
 
# 이미지 다른 파일로 저장
#cv2.imwrite('test.png', img)
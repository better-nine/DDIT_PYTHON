import cv2
import numpy as np
 
# 이미지 읽기
img = cv2.imread('baji.JPG', cv2.COLOR_BGR2GRAY)
img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
re_img = cv2.resize(img_g, dsize=(28, 28), interpolation=cv2.INTER_AREA) 

#이미지 색 반전
out = re_img.copy()
out = 255 - out

img_out = np.reshape(out,(1, 28,28))
print(img_out.reshape) 
 
# 이미지 화면에 표시
cv2.imshow('Test Image', out)
cv2.waitKey(0)

# 이미지 윈도우 삭제
cv2.destroyAllWindows()
 
# 이미지 다른 파일로 저장
#cv2.imwrite('test.png', img)
import cv2
 

img = cv2.imread('lena.jpg', 1) 
 

img90 = cv2.rotate(img, cv2.ROTATE_180)

   
cv2.imshow('Test Image', img90)
cv2.waitKey(0)

# 이미지 윈도우 삭제
cv2.destroyAllWindows()
낭니 청소 열심히해용❤❤❤❤
# 이미지 다른 파일로 저장
cv2.imwrite('lena_180.jpg', img)

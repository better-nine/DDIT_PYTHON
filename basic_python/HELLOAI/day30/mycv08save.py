import cv2
import numpy as np
# 필요한 라이브러리 불러오기
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical

# MNIST 데이터셋 불러오기
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

for i in range(len(train_images)):
    cv2.imwrite('result'+str(i)+'.jpg', train_images[i]) #opencv가 배열(또는 넘피)을 이미지로 바꿔줌 

print("끝") 
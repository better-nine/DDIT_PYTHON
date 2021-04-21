import tensorflow as tf 
import cv2
import numpy as np
from keras.preprocessing import image

  
# 1. Fashion MNIST 데이터셋 임포트
fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images_ori, test_labels) = fashion_mnist.load_data()
   
# 2. 데이터 전처리
train_images, out = train_images / 255.0, test_images_ori / 255.0
 

# 3. 모델 구성
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(512, activation='relu'),
  tf.keras.layers.Dense(10, activation='softmax')
])

# 4. 모델 컴파일
model.compile(optimizer='adam',
          loss='sparse_categorical_crossentropy',
          metrics=['accuracy'])

# 5. 모델 훈련
model.fit(train_images, train_labels, epochs=5 )
 
############################################################################## 
img = cv2.imread('baji.JPG', cv2.COLOR_BGR2GRAY)
img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

re_img = cv2.resize(img_g, dsize=(28, 28), interpolation=cv2.INTER_AREA) 

img2 = 255 - re_img
img_out = np.reshape(img2,(1,28,28))
##############################################################################
predictions = model.predict(img_out)

print("prediction : ", np.argmax(predictions[0])) 



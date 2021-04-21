import tensorflow as tf 
import cv2
import numpy as np
  
# 1. Fashion MNIST 데이터셋 임포트
fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images_ori, test_labels) = fashion_mnist.load_data()
  
# 2. 데이터 전처리
train_images, test_images = train_images / 255.0, test_images_ori / 255.0
  

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
predictions = model.predict(test_images)
 
#-------------------------------- 구글이 예언한 것 _ 여기서 프레딕트 돌린 것_ 비교해서 오차 이미지 집어넣기
correct_num = 0
unmatched_num = 0

for i in range(len(test_labels)):
    pred = np.argmax(predictions[i])
    goog = test_labels[i]
    if pred==goog:
        correct_num += 1
    else:
        unmatched_num +=1
        cv2.imwrite('miss/google_'+str(goog)+'_pred_'+str(pred)+'_'+str(i)+'.jpg', test_images_ori[i])





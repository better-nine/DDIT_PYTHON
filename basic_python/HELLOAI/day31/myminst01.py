import tensorflow as tf
import cv2
  
# 1. Fashion MNIST 데이터셋 임포트
fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

print(len(train_images))
print(len(train_labels))
print(len(test_images))
print(len(test_labels))

for i in range(100):
    cv2.imwrite('train/label'+str(train_labels[i])+'_'+str(i)+'.jpg', train_images[i])

# 2. 데이터 전처리
train_images, test_images = train_images / 255.0, test_images / 255.0

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
 









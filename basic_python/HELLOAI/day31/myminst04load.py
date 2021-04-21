import tensorflow as tf 
import cv2
import numpy as np
from keras.preprocessing import image
 
 
 
model = tf.keras.models.load_model('my_fashion')
############################################################################## 
img = cv2.imread('baji.JPG', cv2.COLOR_BGR2GRAY)
img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

re_img = cv2.resize(img_g, dsize=(28, 28), interpolation=cv2.INTER_AREA) 

img2 = 255 - re_img
img_out = np.reshape(img2,(1,28,28))
##############################################################################
predictions = model.predict(img_out)

print("prediction : ", np.argmax(predictions[0])) 



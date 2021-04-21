from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.models import load_model
import numpy as np
import cv2
import matplotlib.pyplot as plt
import os

# 얼굴 감지
facenet = cv2.dnn.readNet('models/deploy.prototxt', 'models/res10_300x300_ssd_iter_140000.caffemodel')

# 마스크 쓴 얼굴모델
model = load_model('models/mask_detector.model')

cap = cv2.VideoCapture('imgs/mask_test.mp4')

# 비디오의 한 프레임씩 읽습니다.
ret, img = cap.read()

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
out = cv2.VideoWriter('output.mp4', fourcc, cap.get(cv2.CAP_PROP_FPS), (img.shape[1], img.shape[0]))

while cap.isOpened():
    ret, img = cap.read()
    if not ret:
        break

    h, w = img.shape[:2]

    # 이미지 변환
    # 얼굴들을 찾아내고 마스크 여부를 판단한다.
    blob = cv2.dnn.blobFromImage(img, scalefactor=1., size=(300, 300), mean=(104., 177., 123.))
    
    # 변환 이미지를 인풋세팅
    facenet.setInput(blob)
    
    # Face detection 결과를 dets에 저장
    dets = facenet.forward()

    result_img = img.copy()
    
    # 여러개의 얼굴 detection, 얼굴을 하나씩 돌아가면서 찾는 다.
    for i in range(dets.shape[2]):
        confidence = dets[0, 0, i, 2]
        
        # detection 결과에 대한 확신 0.5 이상
        if confidence < 0.5:
            continue
        # 바운딩처리
        x1 = int(dets[0, 0, i, 3] * w)
        y1 = int(dets[0, 0, i, 4] * h)
        x2 = int(dets[0, 0, i, 5] * w)
        y2 = int(dets[0, 0, i, 6] * h)
        
        # 얼굴만 face에 저장
        face = img[y1:y2, x1:x2]
        
        # 전처리하는 부분 리사이즈 
        face_input = cv2.resize(face, dsize=(224, 224))
        face_input = cv2.cvtColor(face_input, cv2.COLOR_BGR2RGB)
        face_input = preprocess_input(face_input)
        face_input = np.expand_dims(face_input, axis=0)
        
        # 마스크를 쓴 확률과 그렇지 않은 확률
        mask, nomask = model.predict(face_input).squeeze()

        if mask > nomask:
            color = (0, 255, 0)
            label = 'Mask %d%%' % (mask * 100)
        else:
            color = (0, 0, 255)
            label = 'No Mask %d%%' % (nomask * 100)

        cv2.rectangle(result_img, pt1=(x1, y1), pt2=(x2, y2), thickness=2, color=color, lineType=cv2.LINE_AA)
        cv2.putText(result_img, text=label, org=(x1, y1 - 10), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.8, color=color, thickness=2, lineType=cv2.LINE_AA)

    out.write(result_img)
    cv2.imshow('result', result_img)
    if cv2.waitKey(1) == ord('q'):
        break

out.release()
cap.release()

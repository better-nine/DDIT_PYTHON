import cv2, json
from flask import Flask,render_template, jsonify, request
import requests

img = cv2.imread('lena.jpg', 1)  
#cv2.imshow('Test Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


def kakao_pic2():
   
    
    API_URL = 'https://dapi.kakao.com/v2/vision/face/detect'
    MYAPP_KEY = '2b712cb6a2c570831e118a005bd718fe'
    
    headers = {'Authorization': 'KakaoAK {}'.format(MYAPP_KEY)}

    try:
        data = { 'image=@lena.jpg' }
        resp = requests.post(API_URL, headers=headers, data=data)
        resp.raise_for_status()
 
        result = json.loads(resp.text)
        print("result",result)
        
        #male: 남자일 확률 / female: 여자일 확률 / age: 추정연령
        male ="%10f" %  result['result']['faces'][0]['facial_attributes']['gender']['male']
        female ="%10f" %  result['result']['faces'][0]['facial_attributes']['gender']['female']
        age = int(result['result']['faces'][0]['facial_attributes']['age'])
        sex =""
        
        #성별
        if male>female:
            sex = "남자"
        else:
            sex = "여자"
        
        return age, sex
        
    except Exception as e:
        print(str(e))
        
    return None
        
age, sex = kakao_pic2()

print(type(age))



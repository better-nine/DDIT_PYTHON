import sys
import requests
import json


API_URL = 'https://dapi.kakao.com/v2/vision/face/detect'
MYAPP_KEY = '2b712cb6a2c570831e118a005bd718fe'

image_url='https://www.sciencetimes.co.kr/wp-content/uploads/2018/10/fc08a3_ecc89ba4706a4199a9a51be9500037d0mv2_d_1754_2480_s_2.jpg'

def detect_product(image_url):
    headers = {'Authorization': 'KakaoAK {}'.format(MYAPP_KEY)}

    try:
        data = { 'image_url' : image_url}
        resp = requests.post(API_URL, headers=headers, data=data)
        resp.raise_for_status() 
         
        return  json.loads(resp.text) 
        
    except Exception as e:
        print(str(e))
        
        sys.exit(0)


aa = detect_product(image_url)
bb = detect_product(image_url)
print(bb)

female = bb['result']['faces'][0]['facial_attributes']['gender']['female']
female = "%10f" % female 
print("남자일 확률 : ","%10f" %  bb['result']['faces'][0]['facial_attributes']['gender']['male'])
print("여자일 확률 : ", female)
# 1보다 작을 경우 숫자 바꿔서 말해도 될 듯 
print("추정나이 : 약",int(bb['result']['faces'][0]['facial_attributes']['age']),"세")
    
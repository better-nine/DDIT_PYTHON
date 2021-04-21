from flask import Flask,render_template, jsonify, request 
import requests
import json
import sys


app = Flask(__name__, static_url_path="", static_folder="static")

@app.route("/kakao_v")    #url-mapping
def kakao_v():
     
    return render_template('kakao_v.html')
    #(출력페이지.html, 같이 보낼 변수 = 초기화)

@app.route("/pic_check", methods=['POST'])
def kakao_pic():
    image_url = request.form["text"]
    
    API_URL = 'https://dapi.kakao.com/v2/vision/face/detect'
    MYAPP_KEY = '2b712cb6a2c570831e118a005bd718fe'
    
    headers = {'Authorization': 'KakaoAK {}'.format(MYAPP_KEY)}

    try:
        data = { 'image_url' : image_url}
        resp = requests.post(API_URL, headers=headers, data=data)
        resp.raise_for_status()
 
        result = json.loads(resp.text)
        
        #male: 남자일 확률 / female: 여자일 확률 / age: 추정연령
        male ="%10f" %  result['result']['faces'][0]['facial_attributes']['gender']['male']
        female ="%10f" %  result['result']['faces'][0]['facial_attributes']['gender']['female']
        age = int(result['result']['faces'][0]['facial_attributes']['age'])
        
        face_info = {"male":male, "female":female, "age":age}
        return jsonify(msg = face_info)
        
    except Exception as e:
        print(str(e))
        sys.exit(0)
     
    return jsonify(msg = {})
        
        
        
if __name__ == "__main__":
    app.run(debug=True)
#   app.run(host='localhost', port=5000)



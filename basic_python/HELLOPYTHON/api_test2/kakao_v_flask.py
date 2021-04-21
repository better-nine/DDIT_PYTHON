from flask import Flask,render_template, jsonify, request 
from bs4 import BeautifulSoup
import requests, math, random
import json
import sys 


app = Flask(__name__, static_url_path="", static_folder="static")

@app.route("/kakao_v2")    #url-mapping
def kakao_v2():
    
    #(출력페이지.html, 같이 보낼 변수 = 초기화)
    return render_template('kakao_v2.html')

@app.route("/pic_check2", methods=['POST'])
def kakao_pic2():
    image_url = request.form["text"]
    
    API_URL = 'https://dapi.kakao.com/v2/vision/face/detect'
    MYAPP_KEY = '2b712cb6a2c570831e118a005bd718fe'
    
    headers = {'Authorization': 'KakaoAK {}'.format(MYAPP_KEY)}

    try:
        data = { 'image_url' : image_url}
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
        
        #연령대
        age_group = math.trunc(age/10)*10 
        #이미지 태그들 
        img_tags = search_soup(age_group, sex)
        print(img_tags)
        
        face_info = {"male":male, "female":female, "age":age, "sex":sex, "age_group":age_group ,"img_tags":img_tags}
         
        #face_result = json.dumps(face_info)
        
        return jsonify(face_info)
        
    except Exception as e:
        print(str(e))
        sys.exit(0)
     
    return jsonify(msg = {})
        

def search_soup(age_group, sex):
    keyword = ['하객룩','옷','신발','의상','모자','겨울옷','여름옷','봄옷','가을옷','코디']
    random.shuffle(keyword)
    
    URL = f'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query={age_group}대+{sex}+하객룩' 
    response = requests.get(URL)
    response.encoding = "UTF-8"
    
    html = response.text #그냥 html형태 그대로 들여쓰기 다나옴
    soup = BeautifulSoup(html, 'html.parser') #들여쓰기 없어진상태로 나옴
    
    #이미지 있는 클래스명 api_get
    #링크 포함 클래스명 shop_product
    imgs = soup.find_all('a',{"class":"thumb"})
    
    link = str(imgs)
     
    return link
    


        
        
if __name__ == "__main__":
    app.run(debug=True)
#   app.run(host='localhost', port=5000)



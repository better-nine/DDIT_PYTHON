from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, sys

#셀레니움 이용해서 나온 설문 문항 빼오기 
#카카오음성 '가져와' 로 명령 내리기
 
def voice_call() :
    import requests
    import json
    import speech_recognition as sr

    url = "https://kakaoi-newtone-openapi.kakao.com/v1/recognize"
    rest_api_key = 'adb174ed9071842964dcd029e2ea63d2'
    
    header = {
        "Content-Type": "application/octet-stream",
        "X-DSS-Service": "DICTATION",
        "Authorization": "KakaoAK " + rest_api_key, }
    r = sr.Recognizer()
    while True :
        with sr.Microphone(sample_rate=16000) as source:
            print()
            print('==== 마이크에 대고 말씀해주세요 ====')
            audio = r.listen(source)
        res = requests.post(url, headers=header, data=audio.get_raw_data())
        try:
            if len(res.text[res.text.index('{"type":"errorCalled"'):res.text.rindex('}')+1])>0 :
                print('음성인식이 안됐습니다')
                continue
        except:
            pass    
        result_json_string = res.text[res.text.index('{"type":"finalResult"'):res.text.rindex('}')+1]
        result = json.loads(result_json_string)
        
        if("종료".__eq__(result['value'])):
            print("====종료되었습니다====")
            break;
    
        if("가져와".__eq__(result['value'])):
            return result['value']
            break;
        else :
            return "음성인식오류"
 
driver = webdriver.Chrome('./chromedriver') #또는 chromedriver.exe
driver.get('http://127.0.0.1:5000/')

driver.find_elements_by_tag_name('a')[3].click()

driver.find_element_by_name('emp_id').send_keys('s00001')
driver.find_element_by_id('pwd').send_keys('1')

driver.find_elements_by_tag_name('input')[2].click()

#############################

if("가져와".__eq__(voice_call())):
    driver.find_elements_by_tag_name('a')[2].click()
    driver.find_element_by_xpath('/html/body/table/tbody/tr/td[1]/table/tbody/tr[2]/td[5]/a').click()

    obj_table = driver.find_element_by_css_selector('body > table > tbody > tr > td:nth-child(1) > table')
    print(obj_table.text)
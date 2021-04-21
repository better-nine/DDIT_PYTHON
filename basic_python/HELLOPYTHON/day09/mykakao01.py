import requests
import json


#//ctrl + shift + F : 제이슨 자동정렬

#url = "https://dapi.kakao.com/v2/search/web.xml"
url = "https://dapi.kakao.com/v2/search/image"
queryString = {"query":"남주혁"}
header = {'authorization':'KakaoAK ce77dea79f432d2469b17f0a81d8a262'}
r = requests.get(url, headers=header, params=queryString)
print(json.loads(r.text))
#print(r.text)

# ! ! ! 현재는 xml을 지원하지 않음 ! ! ! 
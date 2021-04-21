import requests
import json

#선생님이 하시는거

url = "https://dapi.kakao.com/v2/search/image"
queryString = {"query":"남주혁"}
header = {'authorization':'KakaoAK ce77dea79f432d2469b17f0a81d8a262'}
r = requests.get(url, headers=header, params=queryString)

myj = json.loads(r.text)

for i in myj['documents']:
    print(i['collection'],end="\t")
    print(i["datetime"],end="\t")
    print(i["display_sitename"],end="\t")
    print(i["doc_url"],end="\t")
    
    print(i["thumbnail_url"],end="\t")
    print(i["image_url"],end="\t")
    print(i["width"],end="\t")
    print(i["height"])


print(r.text) #string 타입

import requests, math #아나콘다 깔 때 같이 깔림 
from bs4 import BeautifulSoup

age = 33
age_group = math.trunc(age/10)*10 #연령대
sex = "여자" #female

#'https://www.google.com/search?q={}대+{}+쇼핑몰&source=lnms&tbm=isch'.format(age_group,sex)
#f'https://www.google.com/search?q={age_group}대+{sex}+쇼핑몰&source=lnms&tbm=isch'

URL = f'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query={age_group}대+{sex}+쇼핑몰'
response = requests.get(URL)
response.encoding = "UTF-8"

html = response.text #그냥 html형태 그대로 들여쓰기 다나옴
soup = BeautifulSoup(html, 'html.parser') #들여쓰기 없어진상태로 나옴

#이미지 있는 클래스명 api_get
imgs = soup.find_all("img",{"class":"api_get"})
asss = soup.find_all("div",{"class":"shop_product"})
 
link = soup.find_all('a',{"class":"thumb"})
 

print(str(link))

#이미지 들어있는 배열임 
img_tags = [] 
for i in imgs:
    img_tags.append(str(i))

imgsrc = ''.join(img_tags)

#print(imgsrc)

img_tags2 = {}
for i, img in enumerate(imgs):
    img_tags2[i] = img

#print(type(img_tags2))


tds = soup.select('.st2')

for i in tds:
    print(i.find("a")['title'], end="\t")
    print(i.text, end="\t")
    print(i.parent.find_all("td")[1].text)
    #print(i.parent.select_one('td:nth-of-type(2)').text)


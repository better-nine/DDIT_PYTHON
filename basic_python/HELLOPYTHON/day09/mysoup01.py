import requests #아나콘다 깔 때 같이 깔림 
from bs4 import BeautifulSoup

URL = 'https://wikidocs.net/20792' 
response = requests.get(URL) 

html = response.text #그냥 html형태 그대로 들여쓰기 다나옴
soup = BeautifulSoup(html, 'html.parser') #들여쓰기 없어진상태로 나옴

#print(html)
#print(soup)
#print(soup.select('td')) #200:제대로 나옴

tds = soup.select('td')

for i in tds: #배열 안에 있는것들을 뽑아서 i에 삽입
    print(i.text) #태그를 제외한 텍스트 출력





import requests #아나콘다 깔 때 같이 깔림 
from bs4 import BeautifulSoup

URL = 'http://192.168.41.3:7070/HELLOWEB/tel_list.jsp' 
response = requests.get(URL) 

html = response.text
soup = BeautifulSoup(html, 'html.parser')


#print(soup.select('td')) #200:제대로 나옴

tds = soup.find_all('td')

for i in tds: #배열 안에 있는것들을 뽑아서 i에 삽입
    print(i.text) #태그를 제외한 텍스트 출력







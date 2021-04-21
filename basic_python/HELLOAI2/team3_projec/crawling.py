import requests 
from bs4 import BeautifulSoup

keyword = '검색어'

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
        
i = 1        
URL = f'https://search.naver.com/search.naver?where=news&query='+keyword+'&start='+str((10*i)+1)
response = requests.get(URL, headers=headers)
response.encoding = "utf-8"
        
html = response.text  
soup = BeautifulSoup(html, 'html.parser')  

news_titles = soup.find_all('a',{'class':'news_tit'}) 

ahead = 'https://www.saramin.co.kr/zf_user/jobs/relay/view?isMypage=no&rec_idx='

for news_tit in news_titles :
    print(news_tit['title'])
    print(news_tit['href'])
 

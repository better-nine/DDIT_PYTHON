import requests #아나콘다 깔 때 같이 깔림 
from bs4 import BeautifulSoup

URL = 'https://vip.mk.co.kr/newSt/rate/item_all.php' 
response = requests.get(URL)
response.encoding = "euc-kr"

html = response.text #그냥 html형태 그대로 들여쓰기 다나옴
soup = BeautifulSoup(html, 'html.parser') #들여쓰기 없어진상태로 나옴
#print(soup)

'''
n = soup.find_all("td",{"class":'st2'})
#n = soup.find("td",{"class":'st2'}).find("a")["title"]
#test = soup.find("td",{"class":'st2'}).parent.select_one('td:nth-of-type(2)').text

num_name_list=[]
for i in range(len(n)):
    temp=[]
    num = n[i].find("a")["title"]
    name = n[i].text.strip()
    price = n[i].parent.select_one('td:nth-of-type(2)').text
    temp.append(num)
    temp.append(name)
    temp.append(price)
    num_name_list.append(temp)  
    for list in num_name_list:
        print(list)
'''

tds = soup.select('.st2')

for i in tds:
    print(i.find("a")['title'], end="\t")
    print(i.text, end="\t")
    print(i.parent.find_all("td")[1].text)
    #print(i.parent.select_one('td:nth-of-type(2)').text)





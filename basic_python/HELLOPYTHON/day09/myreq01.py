import requests #아나콘다 깔 때 같이 깔림 


URL = 'http://www.tistory.com' 
response = requests.get(URL) 

print(response.status_code) #200:제대로 나옴
print(response.text)


import requests #아나콘다 깔 때 같이 깔림 


URL = 'http://192.168.41.3:7070/HELLOWEB/tel_list.jsp' 
response = requests.get(URL) 

print(response.status_code) #200:제대로 나옴
print(response.text)

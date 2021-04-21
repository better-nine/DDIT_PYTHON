import math
from day10 import mysoup04stock_db
import random
import time
import datetime 


print(time.time())


print(len(mysoup04stock_db.test()))

now = datetime.datetime.now()
formattedDate = now.strftime("%Y%m%d.%H%M")
print(formattedDate)

#list1=[1,2,3,4,5,6,7,8,9,10]

#del list1[10]       # 리스트의 10번째 값을 지웁니다.
#list1.remove(40)    # 리스트에 40이라는 값이 있는 경우 삭제합니다.
                    # 여러개의 값이 있는 경우 가장 앞에 있는 하나만 지워집니다.
                    
# for i in enumerate(list1):
   
print(chr(333))    #문자형캐스팅 아스키코드

rainbow=["빨","주","노","초","파","남","보"]
for i,color in enumerate(rainbow): #dictionary에서는 items()를 사용하면 똑같음
    print("i는: ",i)
    print("color는: ",color) 
    #print('{}번째 색은 {}'.format(i+1,color))
    
print(rainbow)    
random.shuffle(rainbow)
print(rainbow)    
random.shuffle(rainbow)
print(rainbow)    
random.shuffle(rainbow)
print(rainbow)    
    
print(math.pi)    
    
'''   
def get_web(url): #웹사이트 긁어오는 모듈 
    import urllib.request
    response = urllib.request.urlopen(url)
    data = response.read()
    decoded = data.decode('utf-8')
    return decoded
    
url = input('주소값입력:')
content = get_web(url)
print(content) #이건 그냥 html 모양 그대로 긁어옴(들여쓰기있음)
'''
    
#         ↓ 이름표는 문자열 또는 숫자를 주로 사용하지만
dict = {"이름표":[1,2,3]}
#                ↑ 값은 리스트를 포함해서 무엇이든 올 수 있습니다.
print(dict["이름표"])
    
print(list(dict.keys())[0])    
#keys 메서드의 반환값은 리스트가 아니며, 
#리스트로 만들려면 list라는 키워드를 이용해 타입을 변환해야 합니다.
print(list(dict.values())[0][0])
    
print(list(list(dict.items())[0])[1])    
    
    
    
a , b = 1, 2

print(a)

c = (1, 2, 3, 4, 5, 6)
*a, b  = c
print("A",a)


try:
    a = 3/0
except Exception as ex:
    print("에러명:", ex)
# 일부러 에러 일으키는건 raise ValueError 이런식으로 쓰면됨



*a, b = 3, 3, 3
b, *a = 4, 4, 4
print(type(a))


def abcd(*a):
    return a

print(type(abcd(2,)))

def qwe(**a):
    return a

print(type(qwe(a=1,v=a)))

#value = input("입력해주세요>") or '입력 안 하면 False'
#print('결과>',value)
'''
or연산의 결과는  앞의 값이 True이면 앞의 값을,
앞의 값이 False이면 뒤의 값을 따릅니다.

위에서 value 옆에는 or연산이 있기 때문에
input()의 결과값과 or반대편 값을 비교하여
앞이 True라면 앞의 값을 반환하고 False라면 뒤의 값을 반환함
'''

li = ["영","일","이","삼","사"]
print(li.index("일")) #값을 이용해서 위치값을 반환

print(li.extend(["오","륙"])) #리스트 뒤에 값 추가
print(li)

print(li.insert(3,"9")) #세번째 자리에 "9"를 삽입
print(li)

print(li.sort()) #값을 순서대로 정렬 
print(li)

print(li.reverse()) #값을 역순으로 정렬 
print(li)

print(random.shuffle(li)) #랜덤하게 값 섞기
print(li)




    
#별 표현식

a, b, *c = (0,1,2,3,4,5)
print(a)
print(b)
print(c)
# *을 넣으면 뒤에 있는 나머지 숫자가 다 들어가나봄

a, *b = [1,2,3,4,5,6,7,8,9]

print(a)
print(b)

*c, b, a = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]

print(c)
# 거꾸로도 되는듯

a, b, *c = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]

print(c)

a, *b, c = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]

print(b) # 중간도 되는듯. 들어가는 변수의 갯수를 제외한 나머지가 다 들어감 

temp = {}

ice = {'메로나':1000,'폴라포':1200,'빵빠레':1800}

print(ice)

ice.update({'죠스바':1200,'월드콘':1500})

print(ice)
#dictionary는 update() 사용하기

print('메로나 가격:',ice['메로나'])

result = ice.pop('메로나') #이러면 메로나 완전 뽑혀서 dictionary에서 사라짐
print('메로나 가격:',result)
print(ice)

ice = {'메로나': 1000,
       '폴라포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}

ice.update({'메로나':1300})

#update 안 쓰고
ice['메로나'] = 1300
#이렇게 대입해도 됨

print(ice)

del ice['메로나']

print(ice)

l1 = [300,20]
l2 = [400,3]
l3 = [250,100]

inventory = {'메로나':l1, '비비빅':l2,'죠스바':l3}

print(inventory)

a = inventory['메로나'][0]
print(a,'원')

a = inventory['메로나'][1]
print(a,'개')

inventory.update({'월드콘':[500,7]})
print(inventory)

icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}

a = list(icecream.values())
print(a)
#dictionary에서 values 값 뽑아서 리스트로 만들기.
#그냥 values 값만 뽑으면 앞에 values값 뭐시기가 달려있음 그래서 list()로 감싸줌
#왜냐면 요소들이 출력되는거니까 list로 감싸면 됨 

icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}

all = list(icecream.values())
sa = sum(all) #총합계 만들 때 list로 안 만들고 그냥 sum 써도 됨 

print(sa)

icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}

new_product = {'팥빙수':2700, '아맛나':1000}

icecream.update(new_product)

print(icecream)

keys = ("apple", "pear", "peach")
vals = (300, 250, 400)

dic ={}
for i in range(len(keys)):
   dic.update({keys[i]:vals[i]})
print(dic) 
#tuple 두 개를 하나의 dictionary로 합치기
result = dict(zip(keys,vals))
print(result)
#와 진짜 개간단하다 파이썬,,, 별게 다 있네...
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
#이거 꼭 dict(zip(key, vals)) 이렇게 써야하는거같음 앞에 dict인걸 명시해주기
res = dict(zip(date,close_price))
print(res)








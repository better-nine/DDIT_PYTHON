print(3==5)

print(3<5)

print(1 < 4 < 5)

print((3==3)and (4!=3))

print(3>=4)

if 4<3:
    print("gd")

if 4<3:
    print("dd")
else:
    print("aa")

if True:
    print("1",end="")
    print("2")
else:
    print("3")
print("$")

#a = input("입력")

#print(a , a) 

#print(a *3)#String에다 곱하기를 해도 됨


#q = input("숫자")

#print(int(q) + 10)

# ee = input("짝수홀수")
# 
# if int(ee)%2==0:
#     print("짝수")
# else:
#     print("홀수")
# 
# aa = input("입력한 값과 20을 더한 값이 255초과하면 255나옴")
# 
# if int(aa)<=255:
#     print(int(aa)+20)
# elif int(aa)+20>255:
#     print(255)
    
# aa = input()    
# 
# if aa.endswith('00'):
#     print("정각입니다.")
# else :
#     print("정각이 아닙니다.")

a = [1,2,3,4,5]
print(a[-2:])


# fruit = ["사과", "포도", "홍시"]
# 
# qq = input("좋아하는 과일은?")
# if fruit.__contains__(qq):
#     print("정답입니다")
# else:
#     print("x")
#     
# if qq in fruit:
#     print("이렇게해도됨")
# 
# if qq[-1]=="과": #문자열 슬라이싱!!!
#     print("과과과")


# pe = input("투자경고")
# warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
# 
# if pe in warn_investment_list:
#     print("투자 경고 종목입니다")
# else:
#     print("투자 경고 종목이 아닙니다")    


# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# 
# a = input("key값")
# 
# if a in fruit:
#     print("zz")

# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# a = input("value값")
# 
# print("fruit :", fruit.values())
# 
# if a in fruit.values():
#     print("정답")
# else:
#     print("오답")

# a = input("값입력")
# if a.islower():
#     print(a.upper())
# else:
#     print(a.lower())

# score = input()
# 
# a = int(score)
# 
# if a>80:
#     print("A")
# elif a>60:
#     print("B")
# elif a>40:
#     print("C")
# elif a>20:
#     print("D")
# else :
#     print("E")


# b = input("환율액계산")
# 
# if b.endswith("달러"):
#     print(int(b[:2])*1167)
# elif b.endswith("엔"):
#     print(int(b[:2])*1.096)
# elif b.endswith("유로"):
#     print(int(b[:2])*1268)
# elif b.endswith("위안"):
#     print(int(b[:2])*171)


str = "감자튀김"
print(str)
a = str.split()
print(a)


print(3>=4)



print((str+' ')*3)

#a = input()
#b = input()
#c = input()

# if int(a) > 255:
#     print(255)
# else :
#     print(int(a)+20)


# if a.islower() :
#     print('true')
# else :
#     print("else")

# if a > b :
#     if c > a:
#         print(c)
#     else :
#         print(a)
# elif a < b:
#     if c > b:
#         print(c)
#     else :
#         print(b)        

#inp = input()
tel =''

# if inp[:3] == '011':
#     tel = 'SKT'
# elif inp[:3] == '016':
#     tel = 'KT'
# elif inp[:3] == '019':
#     tel = 'LGU'    
# elif inp[:3] == '010':
#     tel = '알수없음'    
# print(f'당신은 {tel} 사용자입니다.')

import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

max = int(btc['max_price'])
min = int(btc['min_price'])

siga = int(btc['closing_price'])

if siga > (max-min):
    print('상승장')
else :
    print("하락장")







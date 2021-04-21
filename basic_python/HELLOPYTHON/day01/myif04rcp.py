import random

# 오늘의 숙제 : 가위바위보 게임 만들기
 
rnd = random.random()

com =""
if rnd > 0.66 :
    com = "가위"
elif rnd > 0.33 :
    com = "바위"
else :
    com ="보"

mine = input("가위/바위/보를 입력하세요")

result = ""
if com==mine :
    result="비김"
elif (com == "가위" and mine == "바위") or (com == "바위" and mine == "보") or (com == "보" and mine == "가위"):
    result = "이김"
elif (com == "가위" and mine == "보") or (com == "바위" and mine == "가위") or (com == "보" and mine == "바위"):
    result = "짐"



print("나 : " + mine)
print("컴퓨터 : " + com)
print("결과 : " + result)

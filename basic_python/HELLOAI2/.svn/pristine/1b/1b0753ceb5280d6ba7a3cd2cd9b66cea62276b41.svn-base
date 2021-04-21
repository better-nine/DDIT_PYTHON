import random
mine = input("가위/바위/보을 입력하세요")

rnd = random.random()

com =""
if rnd > 0.66:
    com = "가위"
elif rnd > 0.33:
    com = "바위"    
else:
    com = "보" 

result = ""

if com == "가위" and mine == "가위"  :
    result = "비김"
elif com == "가위" and mine == "바위"  :
    result = "이김"
elif com == "가위" and mine == "보"  :
    result = "짐"
    
elif com == "바위" and mine == "가위"  :
    result = "짐"
elif com == "바위" and mine == "바위"  :
    result = "비김"
elif com == "바위" and mine == "보"  :
    result = "이김"
    
elif com == "보" and mine == "가위"  :
    result = "이김"
elif com == "보" and mine == "바위"  :
    result = "보"
elif com == "보" and mine == "보"  :
    result = "짐"

    
print("com:"+com)
print("mine:"+mine)
print("result:"+result)


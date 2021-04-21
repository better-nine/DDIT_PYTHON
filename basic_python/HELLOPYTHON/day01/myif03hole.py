import random
# a = input("홀/짝을 입력하세요")
# print(a)
# 주석은 ctrl + /

mine = input("홀 또는 짝을 입력하세요")

rnd = random.random()

# 변수 선언 및 초기화를 동시에 미리 해줘야 바깥에서도 쓸 수 있음. 안에서만 사용할때는 상관없는데
# 나중에 출력할 때 안나옴 
com =""
if rnd > 0.5 :
    com = "홀"
else :
    com ="짝"

result = ""
if com==mine :
    result="이김"
else :
    result = "짐"

print("나 : " + mine)
print("컴퓨터 : " + com)
print("결과 : " + result)

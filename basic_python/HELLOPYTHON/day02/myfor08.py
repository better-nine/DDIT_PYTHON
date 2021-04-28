
a = input("시작 수(큰 수 입력):")
b = input("종료 수(작은 수 입력):")

#숫자 역순으로 찍히는거 만들기 

result = 0;

for i in range(int(b), int(a)+1):
    result = int(a)-i
    print(int(result)+1)
    
    


# int_a = input()
# int_b = input()    
#     
# arr = range(int_a, int_b,-1)
# 
# for i in arr :
#     print(i)

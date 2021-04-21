print("A")
print("B")
print("C")


print('++++')
for i in [100, 200, 300]:
    print('오늘의 메뉴 : ',i+10)
    
for i in ['aaa','dsfasfa','safasfa']:
    print(i, len(i), i[0])
    

for n, i in enumerate([1,2,3]):
    print(3,'x',i,'=',3*i)
    
    
# 리스트 슬라이싱 [시작:끝:증감폭]

a = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
print(a[ : :2]) #2배수번째 요소들 가져오기  
print(a[ :6:2]) #6번째 쉼표까지의 2배수번째 요소 
print(a[6: :2]) #6번째 쉼표부터 2배수번째 요소

print(a[1::1])
print(a[1:])

for i in a[::-1]: #증감폭을 음수로 설정하면 값을 뒤에서부터 거꾸로 가져옴 
    print(i)
    
for i in [3, -20, -3, 44]:
    if i < 0 :
        print(i)
        
for i in [3, -20, -3, 44]:
    if i%3==0 :
        print(i)    
        
for i in [13, 21, 12, 14, 30, 18]:
    if i <20 and i % 3 == 0 :
            print(i)        
        
for i in ["I", "study", "python", "language", "!"]:
    if len(i) >= 3 :
        print(i)     
        
for i in  ["A", "b", "c", "D"]:
    if i.islower() != True: #isupper() 대문자 판별할때 쓸 수 있음 
        print(i)
        
for i in ['dog', 'cat', 'parrot']:
    f = i[0].upper()
    print(f + i[1:])         
        
for i in ['hello.py', 'ex01.py', 'intro.hwp']:
    ab = i.split('.')
    print(ab[0])        
        
for i in ['intra.h', 'intra.c', 'define.h', 'run.py']:
    g = i.split('.')
    if g[1] == 'h':
        print(i)   
        
for i in ['intra.h', 'intra.c', 'define.h', 'run.py']:
    h = i.split('.')
    if h[1]=='h' or h[1]=='c':
        print(i)        
        
        
        
             
        
        
        
           
        
        
        
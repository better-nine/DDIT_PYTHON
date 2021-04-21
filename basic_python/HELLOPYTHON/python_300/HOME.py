'''
 [숙제] 첫날에 100원, 둘째날부터는 전 날의 2배씩 저축을 하려 한다.
       최초로 100만원을 넘는 날은 며칠째이고 해당일의 저축 총액은 얼마인지 구하시오.
'''      
money = 100;        
bank = 100;   
day = 1; 

bank = money
print(day, "일 째 저금 : ",bank)
money = money*2

print("  증가액 : ",money)

while bank < 1000000 :
    
    bank = bank+money
    day = day +1
    print(day,"일 째 저금 : ",bank)
    
    money = money*2
    
    print(" 증가액 : ",money)


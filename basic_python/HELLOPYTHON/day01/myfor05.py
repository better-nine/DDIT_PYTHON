
# 1에서부터 100사이의 3의 배수의 합 

sum = 0

for i in range(1,101) :
    if i % 3 == 0 : 
        sum +=i
        
print(sum)
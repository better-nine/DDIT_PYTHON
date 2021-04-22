
#임시비밀번호 생성
import random, string

alpha = list(string.ascii_letters)
temp_pass = random.randrange(0,999999)
print(''.join(random.sample(alpha,2))+str(temp_pass))
 
  
str = "aa.ad.a.d.jpg"

num = str.count('.')
print(num)

for i in range(num-1):
    str = str.replace('.','',i)

print(str)
 
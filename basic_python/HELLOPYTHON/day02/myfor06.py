
a = input("a=")
b = input("b=")

print(a + "에서" + b +"까지 합은")

result = 0

for i in range(int(a), int(b)+1) :
    result += i
    
print(result)

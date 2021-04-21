
#def 이름 정할때 리턴값 생각해서 지으면 좋을듯
def minmuldiv(a, b):
    return a-b, a*b, a/b

#멀티리턴하려면 쉼표로 잘라서 해주면 됨

min, mul, div = minmuldiv(5, 1)

#----------------------------------------------------

mm = minmuldiv(5, 1)
#이렇게하면 괄호 안에 순차적으로 결과가 출력됨
print(min)
print(mul)
print(div)


print(mm)

#이렇게하면 터짐 
# m1, m2 = minmuldiv(5, 2)
# 
# print(m1)
# print(m2)




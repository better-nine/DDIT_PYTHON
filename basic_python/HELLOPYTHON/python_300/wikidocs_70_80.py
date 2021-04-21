my_variable = ()

movie_rank = ("왜안돼","ㅁㅁㅁㅁ")

print(movie_rank)

num = (1)

print(type(num))

num = (1,)

print(type(num))

t = (1, 2, 3)
# t[0] = 'a'
# print(t)
# tuple은 원소(element)의 값을 변경할 수 없음 

t = 1, 2, 3, 4
#와 미친 괄호없이 그냥 써도 tuple 됨 
print(type(t))

#tuple은 새로 만드려면 아예 기존의 것에 덮어쓰기해서 만들어야함  
t = 'A','b','c'

print(t)

interest = ('삼성전자', 'LG전자', 'SK 하이닉스')

int = [interest[0], interest[1],interest[2]]

print(int)

data = list(interest)
print(data)

interest = ['삼성전자', 'LG전자', 'SK Hynix']

aaa = tuple(interest)
print(aaa)

temp = ('apple','banana','cake')
a, b, c = temp 
print(a, b, c)
#튜플에 들어있는거 옮겨담을수있음
d= temp
print(d)

rrr = tuple(range(2,99,2))
print(rrr)
                #시작값 , 끝값+1 , 증감값
r = tuple(range(2,9,3))
print(r)








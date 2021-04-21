letters = 'python'

let = letters[0]
let2 = letters[2]


print(let, let2)

ll = letters[-3] #음수일 경우 뒤에서부터 뽑아내는듯 
print(ll)

print(letters)

license_plate = "24가 2210"

a = license_plate.split(" ")
print(a[1])

b = license_plate[0:4]
print(b)

string = "가나다라마바사"

stst = string[::1]

print(stst)

sss = "PYTHON"
ssss = sss[::-1]

print(ssss)

# 뒤집어지는건 string만 되는듯
# inttt = 123456789
# iii = inttt[::-1]
# print(iii)

phone_number = "010-8665-7286"
ph = phone_number.split("-")
print(ph[0],ph[1],ph[2])

phnum = "010-8665-7286"
pp = phnum.replace("-", "")

print(pp)

url = "http://sharebook.kr"
uu = url[-2:]
print(uu)

up = url.split('.')
print(up[-1])


strrrr = 'abcdfsdasvascawcawcasfawfa'

atat = strrrr.replace('a', 'A')

print(strrrr)
print(atat)
#문자열은 변경할 수 없는 자료형임. 원본은 그대로 둔 채 새롭게 변경된 문자열 객체를 리턴해줌

print("hey"*3) #문자열에 대한 곱셈은 문자열의 반복을 의미함 

print("-"*80)

t1 = 'python'
t2 = 'java'

t3 = t1+" "+t2 +" "

print(t3*4)

name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13

# %s는 문자열 데이터 값 / %d는 정수형 데이터 타입의 값 
print('이름:%s 나이: %d' % (name1, age1))
print('이름:%s 나이: %d' % (name2, age2))

print('이름:{} 나이:{}'.format(name1, age1))

str = "sometimes i wish"
print('all day long{}{}{}{}{}{}{}'.format(name1,name1,str,name1,name1,name1,name1))


print(str[-4:])


print(f'이름:{name1} 나이:{age1}')

stock = "5,969,782,550"
st = stock.replace(",", "")
s = int(st)

print(type(s))

qua = "2020/03(E) (IFRS연결)"

print(qua[:7])

data = "       삼성전자           "

data2 = data.strip(" ")

print(data2)







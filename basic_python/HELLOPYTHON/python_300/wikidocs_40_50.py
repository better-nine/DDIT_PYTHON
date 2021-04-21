ticker = "btc_krw"

t = ticker.upper()

print(t)

ti = t.lower()

print(ti)

hello = "hello"

he = hello.capitalize()

print(he)

file_name = "보고서.xlsx"
flag = file_name.endswith("xlsx" or "xls")
print(flag)

#보고서로 시작하는 string이기 때문에 False
flag2 = file_name.startswith('2020')
print(flag2)

a = "hello world"
a = a.split(" ")
print(a[0]+a[1])

date = "2020-05-01"
date2 = date.split("-")
print(f'연도:{date2[0]} 월:{date2[1]} 일:{date2[2]}')

print('{}년 {}월 {}일'.format(date2[0],date2[1],date2[2]))


data = "aa        "

d = data.rstrip()
print(d)







































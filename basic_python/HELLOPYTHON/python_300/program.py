



a = ["ada","ss"]

b = "ad".join(a)

print(type(b))



str = "오늘은 날씨가 흐림"

# split()을 이용해서 str을 공백으로 나눈 문자열을 words에 저장하세요
words = str.split(" ")


# index()를 이용해서 "흐림"이 words의 몇번째에 있는지 찾고, 
# position에 저장하세요.
position = words.index("흐림")


words[position] = "맑음"

# join()을 이용해서 words를 다시 문자열로 바꿔 new_str에 저장하세요. 
# words를 문자열로 바꿀때는 공백 한 칸을 기준으로 붙이면 됩니다.
new_str = " ".join(words)


print(new_str)


temp = []
list =[]

for j in range(10):
    temp.append(0)

for i in range(10):
    list.append(temp)

print(list)


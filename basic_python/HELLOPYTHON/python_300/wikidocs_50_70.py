movie_rank = []
movie_rank.append("닥터스트레인지")
movie_rank.append("스플릿")
movie_rank.append("럭키")

print(movie_rank)

movie_rank.append("배트맨")
print(movie_rank)

movie_rank.insert(1, "슈퍼맨")
print(movie_rank)

del movie_rank[3]
# movie_rank.pop(3)
print(movie_rank)

movie_rank.remove('스플릿')
movie_rank.remove('배트맨')
print(movie_rank)

lang1 = ["c","c++","java"]
lang2 = ["python","go","c#"]

langs = lang1 + lang2
#이런미친 그냥 리스트더하기도됨
print(langs)

nums = [1,2,3,4,5,6,7]
max = max(nums)
min = min(nums)
print(max, min)

nums=[1,2,3,4,5]

com = 0
for i in range(len(nums)):
    com += nums[i]
print(com)

print(sum(nums))

cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
print(len(cook))

print(sum(nums)/len(nums))

price = ['20180728', 100, 130, 140, 150, 160, 170]

print(price[1:])

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(nums[::2])

print(nums[1::2])

print(nums[::-1])

interest = ['삼성전자', 'LG전자', 'Naver']

print(interest[0],interest[2])

interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']

print(interest[0],interest[1],interest[2],interest[3],interest[4])
print(" ".join(interest))

print("/".join(interest))

print("\n".join(interest))

string = "삼성전자/LG전자/Naver"
sp = string.split("/")
print(sp)

data = [2, 4, 3, 1, 5, 10, 9]
dd = data.sort() #sort 리턴값 없음 
print(data)
print(dd)

ddd = sorted(data) #sorted는 리턴값 있음 
print(ddd)























from dask.array.random import random
from random import randrange



meal = ["뼈해장국","신가네떡볶이","슈비버거","빵집","안먹기","편의점","짜장면","짬뽕"]

rn = randrange(1,len(meal))
    
eat = meal.pop(rn)

print(eat)




def solution(board, moves):
    answer = 0
    tong = []
    
    for i, move in enumerate(moves):
        if board[move][-1] != 0:
            te = board[move].pop()
            tong.append(te)
            if len(tong)>1:
                if tong[-1]==temp:
                    tong.pop()
                    answer +=1
                else:
                    tong.append(temp)

    return answer



board=[[0,0,0,0,0],
       [0,0,1,0,3],
       [0,2,5,0,1],
       [4,2,4,4,2],
       [3,5,1,3,1]]

moves = [1,5,3,5,1,2,1,4]
temp = 0
print("값테스트",temp)
#aa = solution(board, moves)
#print("aa:" ,aa)
tong =[]
answer = 0

for i, move in enumerate(moves):
    print(i,"번째", move,"째 줄", board[move-1][-1], answer)
    if board[move-1][-1] != 0:
        te = board[move-1].pop()
        tong.append(te)
        if len(tong)>1:
            if tong[-1]==temp:
                tong.pop()
                answer +=1
            else:
                tong.append(temp)
               

print(answer)








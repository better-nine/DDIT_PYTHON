import numpy as np

arr_1 = np.ones((3,3)) #2차원 넘피배열 

#arr_2 = np.reshape(arr_1,(5,3)) #넘피 배열은 열과 행을 뒤집는것도 가능하다



print(arr_1)
#print(arr_2)

arr = [[3,3,3],[3,3,3],[3,3,3]]

from functools import reduce

asd = list(reduce(lambda x, y: x+y, arr))

print("asd : ", asd)

b = np.reshape(arr,(3,3))   #일반 배열을 넘피배열로 활용하는것도 가능함 ! 
                            #일반 배열을 넘피배열로 바꾼 경우는 값 사이가 공백임
                            #일반배열은 값 사이가 쉼표
                            #넘피배열은 값 사이가 온점
print(type(b))

arr = [6,6]
n_arr = np.array(arr)
# c = arr(n_arr)

print(type(arr),":", arr)
print(type(n_arr),":", n_arr)























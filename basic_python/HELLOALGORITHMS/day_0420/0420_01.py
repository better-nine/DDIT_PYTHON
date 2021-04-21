'''
1-1
1부터 n까지 연속한 숫자의 제곱의 합을 구하는 프로그램을 for 반복문으로 만들어보세요
예를들어 n=10이라면 1^2 + 2^2 + 3^2 +... 10^2 = 385 를 계산하는 프로그램입니다.

1-2
연습문제 1-1프로그램의 계산복잡도는 O(1)과 O(n)중 무엇일까요?

1-3
1부터 n까지 연속한 숫자의 제곱의 합을 구하는 공식은 n(n+1)(2n+1)//6 으로 알려져 있습니다. 
for반복문 대신 이 공식을 이용하면 알고리즘의 계산복잡도는 O(1)과 O(n)중 무엇이 될까요?
'''

##############################################
list = [1,2,3,4,5,6]

list.insert(3,4)    #list의 3번 위치에 4를 추가합니다
list.clear()        #list의 모든 자료를 지웁니다
flag = 4 in list    #list 안에 해당하는 값의 존재여부를 반환합니다

'''
1. 첫 번째 숫자 17을 최댓값으로 기억합니다.
2. 두 번째 숫지 92를 현재 최댓값 17과 비교합니다. 92는 17보다 크므로 최댓값을 92로 바꿔 기억합니다.
3. 세 번째 숫자 18을 현재 최댓값 92와 비교합니다. 18은 92보다 작으므로 지나갑니다.
4. ~ 7. 네 번째 숫자부터 일곱 번째 숫자까지 같은 과정 반복
8. 마지막 숫자 42를 현재 최댓값 92와 비교합니다. 42는 92보다 작으므로 지나갑니다.
9. 마지막으로 기억된 92가 주어진 숫자 중 최댓값입니다.
'''
list = [17, 92, 18, 44, 25, 36, 32, 42]
max_num = list[0]

for i in list :
    if max_num < i:
        max_num = i
print(max_num)


sort_list = sorted(list)
print(sort_list[-1])

##############################################
'''
리스트에 숫자가 n개 있을 떼 가장 큰 값이 있는 위치 번호를 돌려주는 알고리즘을 만들어보세요.
'''
idx_num = 0
temp_num = list[0]
for i in range(len(list)) :
    if temp_num < list[i]:
        temp_num = list[i]
        idx_num = i

print(idx_num, list)  

##############################################
'''
숫자 n개를 리스트로 입력받아 최솟값을 구하는 프로그램을 만들어보세요.
'''      
def minimum(p_list):
    mim_num = p_list[0]
    for i in p_list:
        if mim_num > i:
            mim_num = i
    return mim_num

result = minimum(list)
print(result)

##############################################
s = set()           #집합을 생성한다
s.add(3)            #집합안에 값을 삽입한다
s.add(4)            #집합안에 값을 삽입한다
s.add(5)            #집합안에 값을 삽입한다
print(len(s), s)
s.discard(4)        #집합 내 값을 삭제한다
print(len(s), s)

s.clear()           #집합의 모든 자료를 지운다
flag = 3 in s       #집합 안에 들어있는 값 검증
print(flag, s)
'''
n명의 사람 이름 중에서 같은 이름을 찾아 집합으로 만들어 돌려주는 알고리즘을 만들어보세요.
'''
def same_name(list):
    return_set = set()
    for i in range(0, len(list)-1):
        for j in range(i + 1, len(list)):
            if list[i] == list[j]:
                return_set.add(list[i])
    return return_set       

people = ['Mike','Dave','Jane','Paraday','Happy','John','Paraday','Dave']
name_set = same_name(people)

print(name_set)

# ------여기까지 236pg 





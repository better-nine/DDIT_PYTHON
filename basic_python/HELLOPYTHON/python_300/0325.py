participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
def solution(participant, completion):
 
    for i in completion:
        num = participant.count(i)
        participant.pop(num)
        
    return participant[0]
gg = solution(participant, completion)
 
# 윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.
# 예를 들어, 2012년은 4의 배수이면서 100의 배수가 아니라서 윤년이다. 
# 1900년은 100의 배수이고 400의 배수는 아니기 때문에 윤년이 아니다. 
# 하지만, 2000년은 400의 배수이기 때문에 윤년이다.



isinstance(3, 4)

yun = int(input())
if yun % 4 == 0 and yun % 100 != 0 :
    print(1)    
if 400 % yun==0 :
    print(1)    
else :
    print(0)
    
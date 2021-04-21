
answer = []
array = [1,5,2,6,3,7,4]
comm = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]


list_str2=[]
for i in range(len(comm)):
    list_str2 += list(map(str,comm[i]))
    print(list_str2)




def solution(array, commands):
    
    answer = []
    
    for i in range(len(commands)):
        
        tem =[]
        
        if commands[i][0]-1 is not commands[i][1]:
            tem = array[commands[i][0]-1:commands[i][1]]
            print(i,"번째 :",tem)
        else :
            tem = [array[commands[i][1]-1]]
        tem.sort()
    
        num = tem.pop(commands[i][2]-1)
        answer.append(num)
   
    return answer



def solution2(array, commands):
    
    answer = []
    tem = array[commands[0][0]-1:commands[0][1]-1]
    tem.sort()
    print("1 : ", array)
    print("1 : ", tem)
    
    #num1 = tem.pop(commands[0][2]-1)
    #answer.append(num1)
    
    
    if commands[1][1]-1 is not commands[1][1]-1:
        tem = array[commands[1][0]-1:commands[1][1]-1]
    else :
        tem = [array[commands[1][1]-1]]
    tem.sort()
    
    num = tem.pop(commands[1][2]-1)
    answer.append(num)
    
    tem = array[commands[2][0]-1:commands[2][1]-1]
    tem.sort()
    print("3 : ", array)
    print("3 : ", tem)
    
    #num1 = tem.pop(commands[2][2]-1)
    #answer.append(num1)

    #answer.sort()    
    return answer


aaa = solution(array, comm)

print(aaa)





















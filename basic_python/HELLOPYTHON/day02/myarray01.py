arr = [0,1,2,3,4] #배열선언


print(arr)

arr.append(0)
arr.append(1)

print(arr)

arr.insert(0, 3)

print(arr)

arr.remove(3) #앞에거부터 지워짐 

print(arr)

arr.reverse() 

print(arr)

a = arr.copy()

print(a)

b = arr.count(4) #대상이 들어있는 갯수를 반환

print(b)

arr.insert(len(arr), 4) #어레이 맨 마지막에 4를 추가

print(arr)

arr.insert(1, 9) #1번째 방에 9를 대입

print(arr)

arr.append(len(arr))

print(arr)

arr.append("글자도 들어가나?")

print(arr)
 
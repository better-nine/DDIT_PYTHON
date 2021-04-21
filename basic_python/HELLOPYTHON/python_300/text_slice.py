a = 'Life is too short, You need Python'

print(a[19:-7]) #음수값은 뒤에서부터 계산한다. 뒤에 값 제외한다고 생각하면 편할듯 

print(a[:17]) #문자열의 처음부터 끝 번호까지 뽑아냄 

print(a[:]) #문자열 전부 다 뽑아냄 


b = '20210305Rainy'
date = b[:8]    #8을 포함하지 않음 
weather = b[8:] #8을 포함함 

print(date,weather)
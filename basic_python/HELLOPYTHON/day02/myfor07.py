
a = input("출력할 구구단은? ex)2~9")




result =0;

for i in range(1, 10) :
    result = int(a) * i
    print(a, "*" ,i,"=" ,result)

# for i in range(1, 20, 1) : #range(시작값, 끝값, 증감량)
#     print(i)
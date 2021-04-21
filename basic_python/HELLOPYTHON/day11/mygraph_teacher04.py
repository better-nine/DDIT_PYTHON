import cx_Oracle
import matplotlib.pyplot as plt
import numpy as np

connection = cx_Oracle.connect('python','python','localhost:1521/xe')
cursor = connection.cursor()
def getCprice(s_name):    
    sql_str = "select cprice from STOCK where s_name='"+s_name+"' order by in_time"
    cursor.execute(sql_str)
    
    ret=[]
    for name in cursor:
        ret.append(name[0])
   
    return ret

def getSnames():        
    sql_str = "select s_name from stock group by s_name"
    cursor.execute(sql_str)
    
    ret=[]
    for name in cursor:
        ret.append(name[0])
   
    return ret


fig = plt.figure()
ax = fig.gca(projection='3d')  # 보여줄 방식을 3d로 설정합니다.

ax.set_zlabel('Z')
ax.set_ylabel('Y')
ax.set_xlabel('X')

s_names = getSnames() #기업명 들어갈 배열

cnt = len(getCprice(s_names[0])) #항목의 종류를 가진 배열의 길이 
x = np.zeros(cnt) #위치 정해주는 넘피배열 생성 ( 기본값 0 )
y = range(cnt) #수집된 가격의 갯수만큼 배열 생성

for i,name in enumerate(s_names):
    z = np.array(getCprice(name))    
    z_init = z[0]
    if z_init ==0:
        continue
    z = (z/z_init)*100    
    ax.plot(x+i, y, z) 

    
plt.show() #그래프 화면 띄워주는 명령어

cursor.close()
connection.close()

import cx_Oracle
import matplotlib.pyplot as plt
import numpy as np

def getCprice(s_name):    
    connection = cx_Oracle.connect('python','python','localhost:1521/xe')
    cursor = connection.cursor()
    
    sql_str = "select cprice from STOCK where s_name='"+s_name+"' order by in_time"
    cursor.execute(sql_str)
    
    ret=[]
    for name in cursor:
        ret.append(name[0])
   
    cursor.close()
    connection.close()
    return ret



fig = plt.figure()
ax = fig.gca(projection='3d')  # 보여줄 방식을 3d로 설정합니다.

ax.set_zlabel('Z')
ax.set_ylabel('Y')
ax.set_xlabel('X')

s_names = ["삼성전자","LG","SK"] #기업명 들어갈 배열

cnt = len(getCprice(s_names[0])) #항목의 종류를 가진 배열의 길이 
x = np.zeros(cnt)
y = range(cnt)

for i,name in enumerate(s_names):
    z = getCprice(name)
    ax.plot(x+i, y, z) 
    
plt.show() #그래프 화면 띄워주는 명령어


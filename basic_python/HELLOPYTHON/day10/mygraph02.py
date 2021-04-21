import matplotlib.pyplot as plt
import cx_Oracle


fig = plt.figure()
ax = fig.gca(projection='3d')  # 보여줄 방식을 3d로 설정합니다.

ax.set_zlabel('Z')
ax.set_ylabel('Y')
ax.set_xlabel('X')

#연결에 필요한 기본 정보 (유저, 비밀번호, 데이터베이스 서버 주소)
#('유저/비밀번호@데이터베이스서버주소')
connection = cx_Oracle.connect('python','python','localhost:1521/xe')
cursor = connection.cursor()

sql_str = "select cprice,in_time from STOCK where s_name='삼성전자' order by in_time"
cursor.execute(sql_str)

x = [0,0,0,0,0,0,0,0,0,0] #기업명(지정값)
y = [] #시간
z = [] #금액

for name in cursor:
    time = name[1]
    time = time[-4:]
#    x.append(name[0])
    y.append(int(time))
    z.append(name[0])

ax.plot(x, y, z)  #그래프 안에서 선 이어줌 
####################################################################

plt.show() #그래프 화면 띄워주는 명령어

cursor.close()
connection.close()



import cx_Oracle

#연결에 필요한 기본 정보 (유저, 비밀번호, 데이터베이스 서버 주소)
#('유저/비밀번호@데이터베이스서버주소')
connection = cx_Oracle.connect('python','python','localhost:1521/xe')
cursor = connection.cursor()

sql_str = 'select nvl(max(pan)+1,1) as maxpan from omok'
cursor.execute(sql_str)


max_pan=0
for name in cursor:
    max_pan=int(name[0])

print("max_pan : ", max_pan)

cursor.close()
connection.close()
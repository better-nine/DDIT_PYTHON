import cx_Oracle

#연결에 필요한 기본 정보 (유저, 비밀번호, 데이터베이스 서버 주소)
#('유저/비밀번호@데이터베이스서버주소')
connection = cx_Oracle.connect('python','python','localhost:1521/xe')
cursor = connection.cursor()

sql_str = 'select col01, col02, col03 from sample'
cursor.execute(sql_str)

for name in cursor:
    print("테스트 이름 리스트 : ", name[0])

cursor.close()
connection.close()
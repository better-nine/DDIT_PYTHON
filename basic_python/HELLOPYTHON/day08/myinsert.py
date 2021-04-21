import cx_Oracle

#연결에 필요한 기본 정보 (유저, 비밀번호, 데이터베이스 서버 주소)
#('유저/비밀번호@데이터베이스서버주소')
connection = cx_Oracle.connect('python','python','localhost:1521/xe')
cursor = connection.cursor()

sql_str = "insert into sample(col01, col02, col03) values(:1,:2,:3)"
cnt = cursor.execute(sql_str,('77','77','77'))

print(cnt)

connection.commit()



cursor.close()
connection.close()
import cx_Oracle

#연결에 필요한 기본 정보 (유저, 비밀번호, 데이터베이스 서버 주소)
#('유저/비밀번호@데이터베이스서버주소')
connection = cx_Oracle.connect('python','python','localhost:1521/xe')
cursor = connection.cursor()
sql_str = "insert into tetris(LEARN400, ACTION) values(:1,:2)"

cnt = cursor.execute(sql_str,('77','7' ))

cursor.close()
connection.commit()
connection.close()
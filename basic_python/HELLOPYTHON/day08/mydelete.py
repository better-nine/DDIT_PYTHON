import cx_Oracle

#연결에 필요한 기본 정보 (유저, 비밀번호, 데이터베이스 서버 주소)
#('유저/비밀번호@데이터베이스서버주소')
connection = cx_Oracle.connect('python','python','localhost:1521/xe')
cursor = connection.cursor()

sql_str = "delete sample where col01=:1"
cnt = cursor.execute(sql_str,('5',)) #뒤에다 쉼표 한번 더 넣으면 두자릿수도 됨 
#위에 있는 cursor.excute는 리턴값이 없음 


print(format(cursor.rowcount)) #성공했을때 결과값 돌려받는 코드 

connection.commit()



cursor.close()
connection.close()
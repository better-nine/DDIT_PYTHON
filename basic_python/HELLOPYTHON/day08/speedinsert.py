import cx_Oracle # cx: c++ 가져다 쓰는거라서 속도가 개선됨 
import time
# import datetime
# startd = datetime.datetime().now()
# endd = datetime.datetime().now()

connection = cx_Oracle.connect('python','python','localhost:1521/xe')
cursor = connection.cursor()
sql_str = "insert into sample(col01, col02, col03) values(:1,:2,:3)"

start = time.time() #시작시간
for i in range(10000):
    cursor.execute(sql_str,('77','77','77')) # 행운의 77 77 77
end = time.time() #끝시간

connection.commit()
cursor.close()
connection.close()

total = end-start
print(total)
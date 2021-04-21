import cx_Oracle 
from day10 import mysoup04stock_db
import datetime 

now = datetime.datetime.now()
formattedDate = now.strftime("%Y%m%d.%H%M")

connection = cx_Oracle.connect('python','python','localhost:1521/xe')
cursor = connection.cursor()
sql_str = "insert into stock(s_code, s_name, cprice, in_time) values(:1,:2,:3,:4)"

list = mysoup04stock_db.test()

for i in range(len(list)):
    cursor.execute(sql_str,(list[i][0],list[i][1],list[i][2].replace(',',""),list[i][3])) 


print(format(cursor.rowcount))
connection.commit()
cursor.close()
connection.close()
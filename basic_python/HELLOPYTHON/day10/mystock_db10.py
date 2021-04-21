import cx_Oracle 
import time
import datetime 

for j in range(10):
    from day10 import mysoup04stock_db

    connection = cx_Oracle.connect('python','python','localhost:1521/xe')
    cursor = connection.cursor()
    sql_str = "insert into stock(s_code, s_name, cprice, in_time) values(:1,:2,:3,:4)"
    
    list = mysoup04stock_db.test()
    
    now = datetime.datetime.now()
    formattedDate = now.strftime("%Y%m%d.%H%M")
    
    for i in range(len(list)):
        cursor.execute(sql_str,(list[i][0],list[i][1],list[i][2].replace(',',""),formattedDate)) 

    print(format(cursor.rowcount))
    
    
    connection.commit()
    time.sleep(61)  
    
cursor.close()
connection.close()


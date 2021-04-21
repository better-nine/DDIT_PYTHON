import cx_Oracle 

def getMax():
    connection = cx_Oracle.connect('python','python','localhost:1521/xe')
    cursor = connection.cursor()
    
    sql_str = 'select nvl(max(pan)+1,1) as maxpan from omok'
    cursor.execute(sql_str)
    max_pan=0
    for name in cursor:
        max_pan=int(name[0])
    
    return max_pan
    print("max_pan : ", max_pan)

    cursor.close()
    connection.close()


def writeHistory(pan, history, win):
    connection = cx_Oracle.connect('python','python','localhost:1521/xe')
    cursor = connection.cursor()
    
    sql_str = "insert into omok(pan, pseq, history, win) values(:1,:2,:3,:4)"
    
    
    for i, h in enumerate(history):
        cursor.execute(sql_str, (pan, i, h, win))
    
    connection.commit()
    cursor.close()
    connection.close()


   

# max_pan = getMax()
# print(max_pan)

history =[1,2]
pan =1
win = 1

writeHistory(pan, history, win)







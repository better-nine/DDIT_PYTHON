import cx_Oracle

def getData():
    connection = cx_Oracle.connect('python','python','localhost:1521/xe')
    cursor = connection.cursor()
    
    sql_str = 'select col01, col02, col03 from sample'
    cursor.execute(sql_str)
    
    list = []    
    for name in cursor:        
        list.append( {'col01':name[0],'col02':name[1],'col03':name[2]})
    
    cursor.close()
    connection.close()
    return list


def myinsert(col01, col02, col03):
    connection = cx_Oracle.connect('python','python','localhost:1521/xe')
    cursor = connection.cursor()
    
    sql_str = "insert into sample(col01, col02, col03) values(:1,:2,:3)"
    cursor.execute(sql_str,(col01, col02, col03))
    cnt = cursor.rowcount
        
    connection.commit()
    cursor.close()
    connection.close()

    return cnt


def myupdate(col01, col02, col03):
    connection = cx_Oracle.connect('python','python','localhost:1521/xe')
    cursor = connection.cursor()
    
    sql_str = "update sample set col02=:1, col03=:2 where col01=:3"
    cursor.execute(sql_str,(col02, col03, col01))
    cnt = cursor.rowcount
     
    connection.commit()
    
    cursor.close()
    connection.close()
    return cnt


def mydelete(col01):
    connection = cx_Oracle.connect('python','python','localhost:1521/xe')
    cursor = connection.cursor()
    
    sql_str = "delete sample where col01=:1"
    cursor.execute(sql_str,(col01,))  #여기 들어가는게 튜플만 인식해서 뒤에 쉼표를 찍어서 튜플인거 알려줘야함 
    cnt = cursor.rowcount
    
    connection.commit()
    cursor.close()
    connection.close()
    return cnt



# aa = myupdate(6, 5, 5)
# print(aa)

#a = mydelete(6)
#print(a)

#cnt = myinsert(6, 6, 6)
#print(cnt)
    
# list = getData()
# print(list)
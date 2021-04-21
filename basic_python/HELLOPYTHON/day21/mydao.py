import cx_Oracle

class MyDao:
    def __init__(self):  
        self.connection = cx_Oracle.connect('python','python','localhost:1521/xe')
        self.cursor = self.connection.cursor()
        
    def myselect(self):
        self.cursor.execute("select col01, col02, col03 from sample")
        list = []    
        for name in self.cursor:        
            list.append( {'col01':name[0],'col02':name[1],'col03':name[2]})
        return list
        
    def myinsert(self, col01, col02, col03):    
        sql_str = "insert into sample(col01, col02, col03) values(:1,:2,:3)"
        self.cursor.execute(sql_str,(col01, col02, col03))
        self.connection.commit()
        cnt = self.cursor.rowcount
        
        return cnt

    
    def myupdate(self, col01, col02, col03): 
        sql_str = "update sample set col02=:1, col03=:2 where col01=:3"
        self.cursor.execute(sql_str,(col02, col03, col01))
        self.connection.commit()
        cnt = self.cursor.rowcount   
        
        return cnt
    
    def mydelete(self, col01):    
        sql_str = "delete sample where col01=:1"
        self.cursor.execute(sql_str,(col01,))  #여기 들어가는게 튜플만 인식해서 뒤에 쉼표를 찍어서 튜플인거 알려줘야함 
        self.connection.commit()
        cnt = self.cursor.rowcount
    
        return cnt
    
    def __del__(self): #메모리에서 데이터를 지울 때 자동으로 실행되는 친구 
        self.cursor.close()
        self.connection.close()

if __name__ == '__main__':
    dao = MyDao()
    cnt = dao.mydelete(6)
    print(cnt)
    list = dao.myselect()
    print(list)















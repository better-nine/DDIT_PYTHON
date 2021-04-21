import cx_Oracle
import mybatis_mapper2sql

class MyDao:
    def __init__(self):  
        self.connection = cx_Oracle.connect('python','python','localhost:1521/xe')
        self.cursor = self.connection.cursor()
        self.mapper = mybatis_mapper2sql.create_mapper(xml='mybatis_sample.xml')[0]
        print("이게뭘까1 ",mybatis_mapper2sql.create_mapper(xml='mybatis_sample.xml')[0])
        print("이게뭘까2 ",mybatis_mapper2sql.create_mapper(xml='mybatis_sample.xml')[1])
        print("이게뭘까3 ",mybatis_mapper2sql.create_mapper(xml='mybatis_sample.xml'))
        
    def myselect(self):
        sql_str = mybatis_mapper2sql.get_child_statement(self.mapper, "select")
        self.cursor.execute(sql_str)
        list = []    
        for name in self.cursor:        
            list.append( {'col01':name[0],'col02':name[1],'col03':name[2]})
        return list
        
    def myinsert(self, col01, col02, col03): 
        sql_str = mybatis_mapper2sql.get_child_statement(self.mapper, "insert")    
        self.cursor.execute(sql_str,(col01, col02, col03))
        self.connection.commit()
        cnt = self.cursor.rowcount
        
        return cnt

    
    def myupdate(self, col01, col02, col03): 
        sql_str = mybatis_mapper2sql.get_child_statement(self.mapper, "update")
        self.cursor.execute(sql_str,(col02, col03, col01))
        self.connection.commit()
        cnt = self.cursor.rowcount   
        
        return cnt
    
    def mydelete(self, col01):    
        sql_str =  mybatis_mapper2sql.get_child_statement(self.mapper, "delete")
        self.cursor.execute(sql_str,(col01,))  #여기 들어가는게 튜플만 인식해서 뒤에 쉼표를 찍어서 튜플인거 알려줘야함 
        self.connection.commit()
        cnt = self.cursor.rowcount
    
        return cnt
    
    def __del__(self): #메모리에서 데이터를 지울 때 자동으로 실행되는 친구 
        self.cursor.close()
        self.connection.close()

if __name__ == '__main__':
    dao = MyDao()
    #cnt = dao.mydelete(6)
    #print(cnt)
    list = dao.myselect()
    print(list)















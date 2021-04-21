import cx_Oracle
import mybatis_mapper2sql 
from day34_sul.mylog import MyLog

class MyDao_Suser:
    def __init__(self):  
        #self.mylog = MyLog()
        self.connection = cx_Oracle.connect('python','python','localhost:1521/xe')
        self.cursor = self.connection.cursor()
        self.mapper = mybatis_mapper2sql.create_mapper(xml='mybatis_suser.xml')[0] 
        
        
    def mydupl(self, user_id):
        sql_str = mybatis_mapper2sql.get_child_statement(self.mapper, "select_dupl")
        
        #self.mylog.logger.debug(sql_str)
        MyLog().getLogger().debug(sql_str)
            
        self.cursor.execute(sql_str,(user_id,))
        list = []    
        for name in self.cursor:        
            list.append( {'user_id':name[0],'pwd':name[1], 'user_name':name[2], 'birth':name[3], 'mobile':name[4], 'email':name[5], 'in_date':name[6], 'in_user_id':name[7], 'up_date':name[8], 'up_user_id':name[9]})
        
        return list
        
        
    def mylogin(self, user_id, pwd):
        sql_str = mybatis_mapper2sql.get_child_statement(self.mapper, "select_login")
        
        #self.mylog.logger.debug(sql_str)
        MyLog().getLogger().debug(sql_str)
            
        self.cursor.execute(sql_str,(user_id, pwd))
        list = []    
        for name in self.cursor:        
            list.append( {'user_id':name[0],'pwd':name[1], 'user_name':name[2], 'birth':name[3], 'mobile':name[4], 'email':name[5], 'in_date':name[6], 'in_user_id':name[7], 'up_date':name[8], 'up_user_id':name[9]})
        
        return list

    
    def myselect(self):
        sql_str = mybatis_mapper2sql.get_child_statement(self.mapper, "suser_select")
        
        #self.mylog.logger.debug(sql_str)
        MyLog().getLogger().debug(sql_str)
            
        self.cursor.execute(sql_str)
        list = []    
        for name in self.cursor:        
            list.append( {'user_id':name[0],'pwd':name[1], 'user_name':name[2], 'birth':name[3], 'mobile':name[4], 'email':name[5], 'in_date':name[6], 'in_user_id':name[7], 'up_date':name[8], 'up_user_id':name[9] })
        
        return list
    
        
    def myinsert(self, user_id, pwd, user_name, mobile, birth, email, in_date, in_user_id, up_date, up_user_id): 
        sql_str = mybatis_mapper2sql.get_child_statement(self.mapper, "suser_insert")    
        #self.mylog.logger.debug(sql_str)
        MyLog().getLogger().debug(sql_str)
        
        self.cursor.execute(sql_str,(user_id, pwd, user_name, mobile, birth, email, in_user_id, up_user_id))
        self.connection.commit()
        cnt = self.cursor.rowcount
        
        return cnt

    
    def myupdate(self, user_id, pwd, user_name, mobile, birth, email, in_date, in_user_id, up_date, up_user_id): 
        sql_str = mybatis_mapper2sql.get_child_statement(self.mapper, "suser_update")
        #self.mylog.logger.debug(sql_str)
        MyLog().getLogger().debug(sql_str)
        
        self.cursor.execute(sql_str,(pwd, user_name, birth, mobile, email, up_user_id, user_id))
        self.connection.commit()
        cnt = self.cursor.rowcount  
         
        return cnt
    
    def mydelete(self, user_id):    
        sql_str =  mybatis_mapper2sql.get_child_statement(self.mapper, "suser_delete")
        #self.mylog.logger.debug(sql_str)
        MyLog().getLogger().debug(sql_str)
        
        self.cursor.execute(sql_str,(user_id,))  #여기 들어가는게 튜플만 인식해서 뒤에 쉼표를 찍어서 튜플인거 알려줘야함 
        self.connection.commit()
        cnt = self.cursor.rowcount
        
        return cnt
    
    def __del__(self): #메모리에서 데이터를 지울 때 자동으로 실행되는 친구 
        self.cursor.close()
        self.connection.close()
         

if __name__ == '__main__':
    pass















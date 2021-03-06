import cx_Oracle
import mybatis_mapper2sql 
from day41_sul_homework.mylog import MyLog

class MyDao_Snotice:
    def __init__(self):  
        #self.mylog = MyLog()
        self.connection = cx_Oracle.connect('python','python','localhost:1521/xe')
        self.cursor = self.connection.cursor()
        self.mapper = mybatis_mapper2sql.create_mapper(xml='mybatis_suser.xml')[0] 
        
        
    def myselect(self):
        sql_str = mybatis_mapper2sql.get_child_statement(self.mapper, "notice_select")
        MyLog().getLogger().debug(sql_str)
            
        self.cursor.execute(sql_str)
        list = []    
        for n in self.cursor:        
            list.append({'b_seq':n[0],'display_yn':n[1], 'title':n[2], 'content':n[3], 'attach_path':n[4], 'attach_file':n[5], 'hit':n[6], 'in_date':n[7], 'in_user_id':n[8], 'up_date':n[9], 'up_user_id':n[10]})
        return list
 
    def myinsert(self, b_seq, display_yn, title, content, attach_path, attach_file, hit, in_user_id, up_user_id): 
        sql_str = mybatis_mapper2sql.get_child_statement(self.mapper, "notice_insert")    
        MyLog().getLogger().debug(sql_str)

        self.cursor.execute(sql_str,(b_seq, display_yn, title, content, attach_path, attach_file, hit, in_user_id, up_user_id))
        self.connection.commit()
        cnt = self.cursor.rowcount
        
        return cnt

    
    def myupdate(self, b_seq, display_yn, title, content, attach_path, attach_file, up_user_id): 
        sql_str = mybatis_mapper2sql.get_child_statement(self.mapper, "notice_update")
        MyLog().getLogger().debug(sql_str)

        
        self.cursor.execute(sql_str,(display_yn, title, content, attach_path, attach_file, up_user_id, b_seq))
        self.connection.commit()
        cnt = self.cursor.rowcount  
         
        return cnt
    
    def mydelete(self, b_seq):    
        sql_str =  mybatis_mapper2sql.get_child_statement(self.mapper, "notice_delete")
        MyLog().getLogger().debug(sql_str)
        
        self.cursor.execute(sql_str,(b_seq,))  #?????? ??????????????? ????????? ???????????? ?????? ????????? ????????? ???????????? ??????????????? 
        self.connection.commit()
        cnt = self.cursor.rowcount
        
        return cnt
    
    def __del__(self): #??????????????? ???????????? ?????? ??? ???????????? ???????????? ?????? 
        self.cursor.close()
        self.connection.close()
         

if __name__ == '__main__':
    pass
   





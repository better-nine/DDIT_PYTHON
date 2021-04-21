import cx_Oracle
import mybatis_mapper2sql 
from day34_sul.mylog import MyLog

class MyDao_Sresult:
    def __init__(self):  
        #self.mylog = MyLog()
        self.connection = cx_Oracle.connect('python','python','localhost:1521/xe')
        self.cursor = self.connection.cursor()
        self.mapper = mybatis_mapper2sql.create_mapper(xml='mybatis_suser.xml')[0] 
        
    
    def myselect_graph(self, survey_id):
        sql_str = mybatis_mapper2sql.get_child_statement(self.mapper, "myselect_graph")
        MyLog().getLogger().debug(sql_str)
    
        self.cursor.execute(sql_str,(survey_id,))
        list = []    
        for r in self.cursor:        
            list.append({'survey_id':r[0],'s_seq':r[1], 'question':r[2], 'a1':r[3], 'a2':r[4], 'a3':r[5], 'a4':r[6],'c1':r[7],'c2':r[8],'c3':r[9],'c4':r[10]})
        
        return list
    
        
    
        
    def myselect(self):
        sql_str = mybatis_mapper2sql.get_child_statement(self.mapper, "sresult_select")
        MyLog().getLogger().debug(sql_str)

            
        self.cursor.execute(sql_str)
        list = []    
        for name in self.cursor:        
            list.append({'survey_id':name[0],'s_seq':name[1], 'st_mobile':name[2], 'answer':name[3], 'in_date':name[4], 'in_user_id':name[5], 'up_date':name[6], 'up_user_id':name[7] })
        
        return list
    
        
    def myinsert_ans(self, survey_id, st_mobile, ans): 
        anses = ans.split(',')
        sql_str = mybatis_mapper2sql.get_child_statement(self.mapper, "murge_insert")    
        MyLog().getLogger().debug(sql_str)
        
        for num, a in enumerate(anses):
            self.cursor.execute(sql_str,(survey_id, num+1, st_mobile, a))
        
        self.connection.commit()
        cnt = self.cursor.rowcount
        
        return cnt
        
    def myinsert(self, survey_id, s_seq, st_mobile, answer, in_date, in_user_id, up_date, up_user_id): 
        sql_str = mybatis_mapper2sql.get_child_statement(self.mapper, "sresult_insert")    
        MyLog().getLogger().debug(sql_str)

        self.cursor.execute(sql_str,(survey_id, s_seq, st_mobile, answer, in_user_id, up_user_id))
        self.connection.commit()
        cnt = self.cursor.rowcount
        
        return cnt

    
    def myupdate(self, answer, up_user_id, survey_id, s_seq, st_mobile): 
        sql_str = mybatis_mapper2sql.get_child_statement(self.mapper, "sresult_update")
        MyLog().getLogger().debug(sql_str)

        
        self.cursor.execute(sql_str,(answer, up_user_id, survey_id, s_seq, st_mobile))
        self.connection.commit()
        cnt = self.cursor.rowcount 
         
        return cnt
    
    def mydelete(self, survey_id, s_seq, st_mobile):    
        sql_str =  mybatis_mapper2sql.get_child_statement(self.mapper, "sresult_delete")
        MyLog().getLogger().debug(sql_str)
        
        self.cursor.execute(sql_str,(survey_id, s_seq, st_mobile))  #여기 들어가는게 튜플만 인식해서 뒤에 쉼표를 찍어서 튜플인거 알려줘야함 
        self.connection.commit()
        cnt = self.cursor.rowcount
        
        return cnt
    
    def __del__(self): #메모리에서 데이터를 지울 때 자동으로 실행되는 친구 
        self.cursor.close()
        self.connection.close()
         

if __name__ == '__main__':
    pass
   





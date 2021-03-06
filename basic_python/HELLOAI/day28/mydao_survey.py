import cx_Oracle
import mybatis_mapper2sql
from day28.mylog import MyLog

class MyDao_Survey:
    def __init__(self):  
        #self.mylog = MyLog()
        
        self.connection = cx_Oracle.connect('python','python','localhost:1521/xe')
        self.cursor = self.connection.cursor()
        self.mapper = mybatis_mapper2sql.create_mapper(xml='mybatis_suser.xml')[0] 
        
        
        
    def myselect(self, in_user_id):
        sql_str = mybatis_mapper2sql.get_child_statement(self.mapper, "survey_select")
        #self.mylog.logger.debug(sql_str)
        MyLog().getLogger().debug(sql_str)
        
        self.cursor.execute(sql_str,(in_user_id,))
        list = []    
        for name in self.cursor:        
            list.append( {'survey_id':name[0],'title':name[1], 'content':name[2], 'interview_cnt':name[3], 'deadline':name[4], 'in_date':name[5], 'in_user_id':name[6], 'up_date':name[7], 'up_user_id':name[8] })
        return list
    
        
    def myinsert(self, survey_id, title, content, interview_cnt, deadline, in_user_id, up_user_id): 
        sql_str = mybatis_mapper2sql.get_child_statement(self.mapper, "survey_insert")    
        #self.mylog.logger.debug(sql_str)
        MyLog().getLogger().debug(sql_str)

        self.cursor.execute(sql_str,(title, content, interview_cnt, deadline, in_user_id, up_user_id))
        self.connection.commit()
        cnt = self.cursor.rowcount
        
        return cnt

    
    def myupdate(self,survey_id, title, content, interview_cnt, deadline, up_user_id): 
        sql_str = mybatis_mapper2sql.get_child_statement(self.mapper, "survey_update")
        #self.mylog.logger.debug(sql_str)
        MyLog().getLogger().debug(sql_str)
        
        self.cursor.execute(sql_str,(title, content, interview_cnt, deadline, up_user_id,survey_id))
        self.connection.commit()
        cnt = self.cursor.rowcount   
        
        return cnt
    
    def mydelete(self, survey_id):    
        sql_str =  mybatis_mapper2sql.get_child_statement(self.mapper, "survey_delete")
        #self.mylog.logger.debug(sql_str)
        MyLog().getLogger().debug(sql_str)
        
        self.cursor.execute(sql_str,(survey_id,))  #?????? ??????????????? ????????? ???????????? ?????? ????????? ????????? ???????????? ??????????????? 
        self.connection.commit()
        cnt = self.cursor.rowcount
    
        return cnt
    
    def __del__(self): #??????????????? ???????????? ?????? ??? ???????????? ???????????? ?????? 
        self.cursor.close()
        self.connection.close()

if __name__ == '__main__':
    pass














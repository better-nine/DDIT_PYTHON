import mybatis_mapper2sql
mapper, xml_raw_text = mybatis_mapper2sql.create_mapper(xml='mybatis_sample.xml')
# statement = mybatis_mapper2sql.get_statement(mapper)
# statement = mybatis_mapper2sql.get_child_statement(mapper, sql_id) 두번째 자리에 아이디값 넣어주면 해당 내용 불러와짐
 
# statement = mybatis_mapper2sql.get_statement(mapper, result_type='raw', reindent=True, strip_comments=True)
 
statement = mybatis_mapper2sql.get_child_statement(mapper, "select") #xml에서 sql문장 불러와서 statement에다 넣어줌 
print(statement)

statement = mybatis_mapper2sql.get_child_statement(mapper, "insert") #xml에서 sql문장 불러와서 statement에다 넣어줌 
print(statement)

statement = mybatis_mapper2sql.get_child_statement(mapper, "update") #xml에서 sql문장 불러와서 statement에다 넣어줌 
print(statement) 

statement = mybatis_mapper2sql.get_child_statement(mapper, "delete") #xml에서 sql문장 불러와서 statement에다 넣어줌 
print(statement)
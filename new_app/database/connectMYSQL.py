# import mysql.connector
# import DUtil
# database_connection=DUtil.get_db_conn()
# print(database_connection)
# cursor_object=database_connection.cursor()
# student_info_query="create table my_python.student_info(name varchar(30),surname varchar(20),mobile_no varchar(20))"
# #insert_query = "insert into my_python.student_info(name,surname,mobile_no) values(%s,%s,%s)"
# cursor_object.execute(student_info_query)
# database_connection.close()
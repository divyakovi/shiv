# import mysql.connector
# import DUtil
# db_conn=DUtil.get_db_conn()
# cursor_object=db_conn.cursor()
# insert_query="insert into student_info(name,surname,mobile_no) values(%s,%s,%s)"
# val=('divya','kovi','9392676360')
# insert_query="insert into student_info(name,surname,mobile_no) values(%s,%s,%s)"
# val=('satya sowmya latha','talluri','9605324655')
# insert_query="insert into my_python.student_info(name,surname,mobile_no) values(%s,%s,%s)"
# val=[('divya','kovi','9392676360'),('satya sowmya latha','talluri','9605324655'),('akhila','bathineedi','6304188485')]
# cursor_object.executemany(insert_query,val)
# db_conn.commit()
# db_conn.close

import mysql.connector
import DUtil
db_conn=DUtil.get_db_conn()
cursor_obj=db_conn.cursor()
#update_query="update my_python.student_info set mobile_no= 9632501223456 where surname='talluri'"
delete_query="alter table student_info drop surname  "
cursor_obj.execute(delete_query)
print("deleted")
db_conn.commit()
db_conn.close()
print('task done')
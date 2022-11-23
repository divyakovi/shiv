import mysql.connector
import DUtil

def add_student():
    try:
        student_name=input("enter student name:")
        student_surname=input("enter surname:")
        student_mobileno = input("enter mobileno:")
        db_connect=DUtil.get_db_conn()
        cursor_object=db_connect.cursor()
        query="insert into my_python.student_info(name,surname,mobile_no) values(%s,%s,%s)"
        val=(student_name,student_surname,student_mobileno)
        cursor_object.execute(query,val)
        db_connect.commit()
        print("new student is added")
    except Exception as e:
        print("we are experiencing technical issue in adding student,please try after some time",e)
    finally:
        db_connect.close()
    # pass

def update_student():
    try:
        student_Rno = input("enter Rno:")
        student_name=input("enter student name:")
        student_surname= input("enter surname:")
        student_mobileno = input("enter mobile_no:")


        db_connect=DUtil.get_db_conn()
        cursor_object=db_connect.cursor()
        query="update my_python.student_info set name=%s,surname=%s,mobile_no=%s where Rno=%s"
        val=(student_name,student_surname,student_mobileno,student_Rno)
        cursor_object.execute(query,val)
        db_connect.commit()
        print("student record is updated")
    except Exception as e:
        print("we are experiencing technical issue in adding student,please try after some time",e)
    finally:
        db_connect.close()


def deleted_student():
    try:
        student_Rno = input("enter Rno:")
        db_connect=DUtil.get_db_conn()
        cursor_object=db_connect.cursor()
        query="delete from my_python.student_info where Rno=%s"
        val=(student_Rno,)
        cursor_object.execute(query,val)
        db_connect.commit()
        print(" student record is deleted")
    except Exception as e:
        print("we are experiencing technical issue in adding student,please try after some time",e)
    finally:
        db_connect.close()



def get_employee():
    try:
        db_connect=DUtil.get_db_conn()
        cursor_obj=db_connect.cursor()
        query="select * from my_python.student_info"
        cursor_obj.execute(query)
        student_info = cursor_obj.fetchall()
        for student in student_info:
            print(student)
        print("students details fetched successfully")
    except Exception as e:
        print("we are experiencing technical issue in adding a student please try after a while",e)
    finally:
        db_connect.close()
#

if __name__ =='__main__':
    print('welcome to employee management tool')
    print("1.new student")
    print("2.update student")
    print("3.delete student")
    print("4.list employees")
    try:
        selected_option=int(input("please select:"))
    except:
         print("please enter valid input")
    if selected_option not in [1,2,3,4]:
        print("you have selected wrong option")
    else:
        if selected_option ==1:
            add_student()
        elif selected_option ==2:
            update_student()
        elif selected_option ==4:
            get_employee()
        else:
            deleted_student()


# #import divya.png
# x=['grapes','bananas','apple']
# # x.sort(reverse=True)
# # print(x)
# y='python'
# print(sorted(y))
# print(y)


# import smtplib
# my_email="testingemail@gmail.com"
# password="mypw123"

# connection=smtplib.SMTP("smtp.gmail.com",587)
# connection.starttls()
# connection.login(user=my_email,password=password)
# connection.sendmail(from_addr=my_email,to_addrs="receipentemail@gmail.com",msg="Hello Friend")
# connection.close()

# pip install pyjokes
# import pyjokes
# Create a class that will accept the string extract the number from string and convert remaining string
# into asscci converted string Ex:'A1B2c3'  output:# Extracted number is 123 after extracting number string become : ABc
# Ascci converted string is :656699

# def python():
#     return python()+1
# print(python)
# x='python'
# def A(a):
#     a=a.int(input("enter a val:"))
#     return[a:]
#     print(
# A="Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!"
# print (A)

#4.Write a Python program to count repeated characters in a string.
# x='thequickbrownfoxjumpsoverthelazydog'
# print("repeated characters are: ")
# for i in range(0, len(x)):
#     count = 1
#     for j in range(i + 1, len(x)):
#         if (x[i] == x[j] and x[i] != ' '):
#             count = count + 1
#             x = x[:j] + '0' + x[j + 1:]
#     if (count > 1 and x[i] != '0'):
#         print(x[i], " - ", count)
# atuple=1,2,3
# a,b,c=atuple
# print(a)
# class cars:
#     def __init__(self,m,p):
#         self.model=m
#         self.price=p
# audi=cars("R8",1000000)
# print(audi.model)
# print(audi.price)

from zipfile import *
f=ZipFile('file.zip','w',ZIP_DEFLATED)
f.write('java.txt')
f.write('list.py')
f.close()
print("file zipped successfully")
# f=open("divya.png","rb")
# bytes=f.read()
# print(bytes)
# f.close()
# f=open("navya.png","wb")
# f.write(bytes)
# f.close()
# import os
# print(os.getcwd())
# f.write("hi people")
# print(f.write("hey hi"))
# f.seek(4)
# print(f.tell())
# print(f.read())
# f.close()
# f=open("divya.jpg",'r+')
# f.write(bytes)
# print(f.write("photo"))

# f=open("mynewfile.txt",'wb')
# f.write(bytes)
# f.close()
# f=open("mynewfile.txt",'rb')
# f.read()
# f=open("myphoto.jpeg","rb")
# bytes=f.read()
# print(bytes)
# f.close()
# f=open("maa_.jpeg","wb")
# f.write(bytes)
# f.close()
# import os
# print(os.getcwd())

# x=[1,5,2,6,8,3]
# y=[]
# z=[]
# for i in x:
#     if i%2==0:
#         y.append(i)
#         y.sort()
#     else:
#         z.append(i)
#         z.sort()
# out=y+z
# print(out)

# print("this line will be printed")
# x=1
# if x==1:
#     print('x is 1.')
# print("hello world !")
# hello='hello'
# world='world'
# helloworld=hello+world
# print(helloworld)

# mystring='hello'
# myfloat=10.0
# myint=20
# if mystring=='hello':
#     print("string:%s"%mystring)
# if isinstance(myfloat,float)and myfloat==10.0:
#     print("float:%f"%myfloat)
# if isinstance(myint,int)and myint==20:
# #     print("integer:%d"%myint)
# import pywhatkit
# import pyautogui
# pywhatkit.sendwhatmsg('+7036808379','hi dude GoOD morninG',8,34)
# pyautogui.press('enter')

# x={"apples":3,"bananas":4,"lemons":5,"pears":7}
# y=["apples","lemons"]
# z={key:x[key] for key in y}
# print(z)
#
#
# import os
# try:
#     print(10-20)
#     # print("hello world")
#     # os._exit(0)
#     #
#     print(10 / 0)
#     print("hi")
#     #os._exit(0)
# except Exception as e:
#     print("eco friendly")
#     os._exit(0)
#     print("meow")
# finally:
#     print("true")
# import keyword
# print(keyword.kwlist)
# print(len(keyword.kwlist))
# a=2344
# print(type(a))
# a=float(a)
# print(type(a))
# print(a)
# a=int(a)
# print(type(a),a)
a=52
b=58
# a,b=b,a
# print(a)
# print(b)
# temp=a
# a=b
# b=temp
# print(a,b)
# a=a*b
# print(a)
# b=a//b
# print(b)
# a=a//b
# print(a)
# print(a,b)
# a=a+b
# b=a-b
# a=a-b
# print(a,b)
# a=a^b
# b=a^b
# a=a^b
# print(a,b)
# x=[[1,2,3],[4,5,6],[7,8,9,10,11,12]]
# y=[]
# for i in range(len(x)):
#     for j in range(len(x[i])):
#         y.append(x[i][j])
# print(y)

# x=[[1,2,3,4],[2,3,5,6],[38,45,'dfui']]
# y=[]
# for i in (x):
#     for j in i:
#         print(j,end=' ')
# print(y)
# x=[[1,2,3],[4,5,6],[7,8,9],[3,4,5,6,7,8],[1]]
# y=0
# for i in x:
#     temp=len((i))
#     if temp>y:
#         y=temp
# print(y)
# def visits(x):
#     y=0
#     for i in x:
#         temp=len(i)
#         if (temp)>y:
#             temp=y
#     return y
# (visits([[1,2,3],[4,5,6],[7,8,9],[3,4,5,6,7,8],[1]]))


# def max_visits(visits_by_patient):
#     ''' (list of list of it) -> int
#
#     Return the maximum number of visits made by any paitent
#     >>> max_visits([[2, 6], [3, 10], [15], [23], [1, 8, 15, 22, 29], [14]])
#     5
#     '''
#     max_so_far = 0
#     for patient_list in visits_by_patient:
#         visits = len(patient_list)
#         if (visits) > max_so_far:
#             max_so_far = visits
#     return max_so_far
# z=max_visits([[2, 6], [3, 10], [15], [23], [1, 8, 15, 22, 29], [14]])
# print(z)


# print(x[0][1],x[1][1],x[2][1])

# y=[]
#
# for i in range(len(x)):
#     for j in range(len(x[i])):
#         y.append(x[i][j])
#         if y%2==0:
#             print(y)


####### pytest coding of parameterize
# import python_test
# import pytest
# # import sys
# # @pytest.mark.skipif(sys.version_info < (3, 3), reason ="do not run number and test")
# @pytest.mark.parametrize('x, y, result',
#                         (
#                              (7,3,10),
#                              ('hello', 'world', 'helloworld'),
#                              (10.5,20.5,31)
#                         )
#                         )
# def test_add(x,y,result):
#     assert python_test.add(x,y) ==result
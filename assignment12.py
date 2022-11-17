# 1.what are the modes in file handling ? what are they ?

# r-> read mode: This mode is used to read the data in a existing file.the file pointer is positioned at the begining of
# the file.if the specified file does not exists then we will get file not found error

# w->write mode: This mode is used to write the data in a existing  file if the file already contains some data then it
# will be overridden.if the spcified mode is not available then this mode will create a file

# a->append mode:open an existing file for append operation it won't override the data if the specified file is not there
# then it will create a new file

# r+-> read and write mode: This function is used to read and write the data of an existing file

# w+->write and read mode:This function is used to write and read the data and it will overrride the existing data

# a+->To write and read the data it wont override the existing file data



# 2.How to create the file ? how many ways we can create the file ?

# To create a file:
# step:1 open("filenaeme",'w')
# step:2 write some data
# step:3 close the file
# step:4 check wheather the file is created or not by using 'print' statement

# we can create a file in 4 ways. they are :
# by using write mode(w)
# by using write read mode(w+)
# by using append mode(a)
# by using append and read mode(a+)


# # 3.extract all keywords from python file ?Ex: sample.py
#
# def python():
#     a = 100
#     if a > 10:
#         return a
#     else:
#         return b
# import keyword
# print(keyword.kwlist)
# for i in keyword.kwlist:
#     if i==python():
#         print(i)

# sample=python()
# print(sample)
# import keyword
# y=print(keyword.kwlist)
# keywords=keyword.kwlist.extract_keywords(def python():
#     a = 100
#     if a > 10:
#         return a
#     else:
#         return b)
# keywords_list=list(dict(keywords).keys())
# print(keywords_list)
# Output = ['def', 'if', 'return', 'return']
#
# 4.what are decortor, generator, iterator with example ?
# decorator:
# decorator is a function which takes a function as argument and extend its functionality and returns modified function
# with extended functionality
# ex:
# def Abc(fun):
#     print("hello world!")
#     def B():
#         print(123)
#         return fun()
#     return B()
# @Abc
# def C():
#     print("let's do it")
# o/p:
# hello world!
# 123
# let's do it
#generator:generator is a function which is responsible to generate a sequence of values
#we can write generator functions just like ordinary functions but it uses 'yield' keyword to return values
#ex:
# def fun():
#     yield'python'
#     yield'java'
#     yield'apple'
#     yield'coffee'
#     yield'tea'
# g=fun()
# for i in g:
#     print(i)
#     if i=='coffee':
#         break
# print(g.__next__())

# o/p:
# python
# java
# apple
# coffee
# tea
#iterator:iterator in python is an object that is used to iterate over iterable objects like list,tuple,dict and set
# x={1,2,3,4,5,67,78,90,65}
# y=iter(x)
# print(y.__next__())
# print(y.__next__())
# print(y.__next__())
# print(y.__next__())
# print(y.__next__())
# print(y.__next__())
# print(y.__next__())
# print(y.__next__())
# print(y.__next__())
#print(y.__next__())


# 5.create two files read data from one file and write data in another file.
# hint: Make first and last words capital
# from sample1.py Ex : sample1.py python is good java is good all students are good
# output : sample2.py
# PYTHON is GOOD
# JAVA   is GOOD
# ALL students are GEMS

# f=open("assfile.txt",'w')
# f.write('python is good\n')
# f.write('java is good\n')
# f.write('all students are good\n')
# f.close()
# with open("assfile.txt",'r+') as f:
#     text=f.read()
#     print(text)
#     print("current cursor position:",f.tell())
#     f.seek(10)
#     print("current cursor position:",f.tell())
#     f.write("GOOD")
    # f.seek(0)
    # text = f.read()
    # print(text)
    #print("current cursor position:", f.tell())
#     f.seek(0)
#
#print("current cursor position:", f.tell())
#f.write("PYTHON")
# f.seek(0)
# text = f.read()
# print(text)
# print("current cursor position:", f.tell())
#     f.seek(16)
#     print("current cursor position:", f.tell())
#     f.write("JAVA")
#     f.seek(0)
#     text=f.read()
#     print(text)
#     print("current cursor position:", f.tell())
#     f.seek(24)
#     print("current cursor position:", f.tell())
#     f.write("GOOD")
# f.seek(0)
# text=f.read()
# print(text)
# print("current cursor position:", f.tell())
# f.seek(30)
# print("current cursor position:", f.tell())
# f.write("ALL")
# f.seek(0)
# text = f.read()
# print(text)
# print("current cursor position:", f.tell())
# f.seek(47)
# print("current cursor position:", f.tell())
# f.write("GEMS")
# f.seek(0)
# text=f.read()
# print(text)
# f.close()
# f=open("ass_2.txt",'w')
# f.write(text)
# print(f)
# f.close()
# o/p:PYTHON is GOOD
# JAVA is GOOD
# ALL students are GEMS

# 6) what is pickling and unpicking with example ?
#pickling:the process of writing object data to the file is called pickling
# class A():
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def display(self):
#         print("name:",self.name)
#         print("salary:",self.salary)
# obj=A("dev",40000)
# obj.display()
# 7). how to add new data to the existing file ?
# Ex : sample1.py
# python is good
# java is good
# all students are good
# output : sample1.py
# "HELLO FRIENDS" python is good
# "HELLO FRIENDS" java is good
# "HELLO FRIENDS" all students are good
# data1="python is good"
# data2="java is good"
# data3="all students are good"
# f=open("abc.txt","a")
#
# with open("abc.txt","r+") as f:
#     text=f.readlines()
#     print(text)
#     print("the current cursor position:",f.tell())
#     f.seek(0)
#     print("the current cursor position:",f.tell())
#     f.writelines(("hello friends"))
#     f.seek(0)
#     text=f.readlines()
#     print("data after modification:")
#     print(text)
# 8) what are seek() and tell() funtions and what is the use of the that?
# seek():
# we can use seek() method to move cursor(file pointer)to specified location
# data="we are students"
# f=open("xyz.txt","w")
# f.write(data)
# f.close()
# with open("xyz.txt","r+")as f:
#     text=f.read()
#     print(text)
#     print("the current cursor position:",f.tell())
#     f.seek(7)
#     print("the current cursor position:",f.tell())
#     f.write("developers")
#     f.seek(0)
#     text=f.read()
#     print("data after modification:")
#     print(text)

#tell():
#we can use tell() method to return current position of the cursor position of the cursor (file pointer) from begining
# of the file
#the position(index) of the first character in files is zero just like starting index
# f=open("java.txt","w")
# f.write('python python\n')
# f.write('welcome \n')
# f.close()
# f=open("java.txt","r+")
# print(f.tell())
# print(f.read(4))
# f.seek(0)
# print(f.read(3))
# print(f.tell())
# f.close()


# 9) Extract only functions from python file and write in another file ?
#
# ex : sample1.py x= 10
# y = 20
# def Python():
#     print("PYTHON IS GOOD")
# print(x)
# print(y)
# def java():
#     print("java IS GOOD")
# print("we are friends")
# def Total():
#     print("All languages are good")
# print("ALL THE BEST FOR ALL STUDENTS")
# output: sample_output.txt
# def Python():
#     print("PYTHON IS GOOD")
# def java():
#     print("java IS GOOD")
# def Total():
#     print("All languages are good")

# 10.read the data from one file and print data reverse the data another file in reverse order
# ex: sample.txt
# HELLO FRIENDS
# HI STUDENTS
# output_Sample.txt
# FRIENDS HELLO
# STUDENTS HI
# Hint: 1) first reverse the line by line
# 2) reverse the each and every word in same line


# f=open("file.txt","w")
# f.write('HELLO FRIENDS\n')
# f.write('HI STUDENTS\n')
# print("file created successfully")
# f.close()
# f1 = open("output_sample.txt", "w")
# with open("file.txt", "r") as myfile:
#     data = myfile.read()
# data_1 = data[::-1]
# f1.write( data_1)
# print("data reversed sucessfully")
# f1.close()

f=open("file.txt","w")
f.write('HELLO FRIENDS\n')
f.write('HI STUDENTS\n')
print("file created successfully")
f.close()
f1=open("file.txt")
A=f1.readlines()
for i in reversed(A):
    print(i)


j=str(i)
k=j.split()[::-1]
# out=[]
# for rev in k:
#     out.append(rev)
#     print(" ".join(out))
print(k)
# print(" ".join(k))
f1.close()


#oops: object oriented programming system
#class: class is a keyword, class is a collection of objects and methods and variables.
#object: object is the blueprint of class
# class A:
#     def __init__(self):
#         print("maximum")
# # obj=A
# # obj.python(2)
# A()
# class B:
#     def __init__(self,a,b):
#         print(a+b)
#     def C(self):
#         print("minimouse")
# B.C(1)
# B(89,3456)

# class student:
#     def __init__(self,studentname,rno,marks):
#         self.a=studentname
#         self.b=rno
#         self.c=marks
#     def display(self):
#         print("studentname:{}\n rno:{}\n marks{}".format(self.a,self.b,self.c))
# a=student('ram',55,90)
# student.display(a)


#variables are of 3 types they are: static instance and local variables
#instance: if the value of a variable is varied from object to object, then such type of variables are called as instance variables
#for evrey object a separate copy of instance variable is created

# class employee:
#     def __init__(self):
#         self.ename='ram'
#         self.eno=23
#         self.esal=300000
# print(employee().__dict__)   #{'ename': 'ram', 'eno': 23, 'esal': 300000}
# class employee:
#     def __init__(self):
#         self.ename='ram'
#         self.eno=23
#         self.esal=300000
# obj=employee()
# del obj.eno
# print(obj.__dict__)
# obj.d=40
# print(obj.__dict__)
# class test:
#     def __init__(self):
#         self.a=10
#         self.b=20
# t1=test()
# t2=test()
# del t1.a
# print(t1.__dict__)
# t2.a='python'
# t2.b='A1w23Bc'
# print(t2.__dict__)
# class Test:
#     a=10
#     def __init__(self):
#         Test.b=20
#     def m1(self):
#         Test.c=30
#     @classmethod
#     def m2(cls):
#         cls.d1=40
#         Test.d2=400
#     @staticmethod
#     def m3():
#         Test.e=50
# print(Test.__dict__)
# t=Test()
# #print(t.__dict__)
# t.m1()
# #print(t.__dict__)
# t.m2()
# #print(t.__dict__)
# t.m3()
# #print(t.__dict__)
# t.f=60
# print(t.__dict__)
#polymorphism: An entity which represents multiple forms is known as polymorphism
#operator overloading
#method overloading
#constructor overloading
# class duck:
#     def talk(self):
#         print("quack quack")
# class dog:
#     def talk(self):
#         print("bow bow")
# class frog:
#     def sounds(self):
#         print("beck beck")
# obj=[duck(),dog()]
# for i in obj:
#     print(i)
# class book:
#     def __init__(self,pages):
#         self.pages= pages
#     def __add__(self,other):
#         return self.pages+ other.pages
# t2=book(459)
# t1=book(567)
# print("total pages:",t2+t1)
#method overloading:
# class A:
#     def m1(self):
#         print("no arg method")
#     def m1(self,a):
#         print("one aarg method")
#     def m1(self,a,b):
#         print('two args were given')
# obj=A()
# obj.m1()
# obj.m1(56,56)
# class A:
#     def student(self,name='krish',rno=7,marks=99):
#         if name!=None and rno!=None and marks!=None:
#             return name,rno,marks
#         else:
#             print('hola!')
# obj=A()
# print(obj.student('krish',7,99))
# class B():
#     def __int__(self,*d):
#         print("YOLO")
# obj=B(12,3,4,5,6,7,899,8,7655)
#polymorphism:
#hasattr:has attr useful to check the method is exists or not in particular class
# class duck:
#     def talk(self):
#         print('quack quack')
# class human:
#     def talk(self):
#         print('talk talk')
# class dog:
#     def bark(self):
#         print('bow bow')
# x=[duck(),human()]
# for i in x:
#     i.talk()
# def f1(obj):
#     if hasattr(obj,'talk'):
#         obj.talk()
#     elif hasattr(obj,'bark'):
#         obj.bark()
# x=[duck(),human(),dog()]
# for obj in x:
#     f1(obj)
# d=duck()
# f1(d)
# h=human()
# f1(h)
# d=dog()
# f1(d)
# class A:
#     def python(self):
#         print("calling python")
#     def java(self):
#         print("calling java")
# obj=A()
# if hasattr(obj,'python') and hasattr(obj,'java'):
#     obj.java()
#     obj.python()
# elif(hasattr(obj,'divya')):
#     obj.divya()
# a=10
# b=30
# print(a.__add__(b))
# class P:
#     def property(self):
#         print('gold')
#     def marry(self):
#         print('divya')
# class C(P):
#     def marry(self):
#         print('divvi')
#         super().marry()
# c=C()
# c.property()
# c.marry()
#
# class me:
#     def __init__(self):
#         print("parent class")
# class d(me):
#     def __init__(self):
#         print('child class')
#         super().__init__()
# c=d()
# c=me()
# c.__init__()

#CSV: comma separated values
# import csv
# with open("emp.csv",'w',newline="")as f:
#     w=csv.writer(f)
#     w.writerow(["eno","e_name","e_salary"])
#     n=int(input("enter no of employees:"))
#     for i in range(n):
#         x=[]
#         eno=input("enter employee no:")
#         x.append(eno)
#         e_name=input("enter employee name: ")
#         x.append(e_name)
#         e_salary=input("enter employee salary:")
#         x.append(e_salary)
#         w.writerow([eno,e_name,e_salary])
#         print("total data have been written in CSV file")
# import csv
# f=open("emp.csv","r")
# r=csv.reader(f)
# data=list(r)
# print(data)
# for line in data:
#     for word in line:
#         print(word,"\t",end='')
#     print()













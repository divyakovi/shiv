#1.x=[25,35,53,25,52,35,25].remove duplicate elements from the list?
x=[25,35,53,25,52,35,25]
# print(x)
# y=set(x)
# print(y,type(y))
# a=list(y)
# print(a,type(a))
# output:
# [25, 35, 53, 25, 52, 35, 25]
# {25, 35, 52, 53} <class 'set'>
# [25, 35, 52, 53] <class 'list'>
# a=set(x)
# print(a,type(a))
# b=list(a)
# print(b,type(b))

#2.write a program that weather number exists in or not in x
#ex:x=[1,5,7,9] n-->take from input(use input function)check n is exists or not in x
#hint: step 1: use for or while loop.
#step 2: use if statement to check num exists or not
# x=[1,5,7,9]
# x=input("enter x val:")
# print(x)
# print(type(x))
# x=int(x)
# print(type(x))
# x=int(input('enter x val:'))
# print(x)
# for i in range(x):
#     print(i,end=' ')
# print()
# output:
# enter x val:5
# 5
# <class 'str'>
# <class 'int'>
# enter x val:4
# 4
# 0 1 2 3
# print(5 in x)           #x=[1,5,7,9]
# print(9 in x)
# print(6 in x)
# print(4 not in x)
# output:
# True
# True
# False
#True
# for i in x:
#     if i in x:
#         print(i,end=' ')
#     else:
#
#         print("nothing to print")
# o/p: 1 5 7 9


#3.What is the output of below code?
# if(1):
#     print('hi')
# else:
#     print('hello')
# output:
#  hi


# 4.
# a=2
# a=a<<2
# print(a)
# if(a<10):
#     print('python')
# else:
#     print('java')
# output:
# python


#5.write a code for if, if-else, if-elif, nested if?
#if: it is used to check the condition of the given statement weather true or false.if it is true it'll execute the given
#statement
#code:
# x=24
# if(x>20 and x<=24):
#     print('hi')
#     print('hello')
# output:
# hi
# hello
# a=13
# if(a>30):
#     print('false')  #so the given condition is false then there is nothing will be printed in the output

#if-else: it is used to check the condition of the given statement weather true or false.if it is true it'll execute the
# given statement if the condition is false then else statement will be executed
#code:
# a=9
# if(a>1,a<5):
#     print('divya')
# else:
#     print('navya')
# output:
#  divya
# a=10
# if(a>20 and a<6):
#     print('divya')
#     print('kovi')
# else:
#     print('navya')
#     print('kovi')
# output:
# navya
# kovi
#if-elif:it is useful to check multiple conditions. if the condition for if is false, it checks the condition of the
# next elif block and all the remaining sentences, if all the conditions are false then else is executed
#code:
# x=99
# y=49
# if(x<100):
#     print('hey python')
# elif(x>=99):
#     print('ever onward')
# else:
#     print('all are false')
# output: hey python
# if(x<y):
#     print('universe')
# elif(x>y):
#     print('gallexy')
# else:
#     print('milky way')
# output: gallexy


#6.What will be the output after the following statements?
# x=15
# if(x>15):
#     print(0)
# elif x==15:
#     print(1)
# else:
#     print(2)
# output: 1


#7.What will be the output after the following statements?
# x=50
# if x>10 and x<15:
#     print('true')
# elif x>15 and x<25:
#     print('not true')
# elif x>25 and x<35:
#     print('false')
# else:
#     print('not false')
#output: not false


#8.What will be the output after the following statements?
# x=70
# if x<30 or x>=100:
#     print('true')
# elif x<=50 and x==50:
#     print('not true')
# elif x>=150 or x<=75:
#     print('false')
# else:
#     print('not false')
# output: false


#9.What is the a value?
# a=5
# a=+5
# if(0):          #if condition does'nt exist
#     a=a+4
# elif(a<10):
#     a=a>>2
# print(a)
# output:1


#10.What will be the output after the following statements?
# x=40
# y=25
# if(x+y)>=100:
#     print('true')
# elif x+y==50:
#     print('false')
# elif x+y<=90:
#     print('false')
# else:
#     print('not false')
# output: false
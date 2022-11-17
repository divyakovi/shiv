#1.write a syntax for and write an example?
# syntax:for var_name in collection(str,list,set,range,tuple,)
# example:
# a=[1,2,3,4,56,76,89,90]
# print(a)
# for i in a:
#     print(i,end=' ')
# print()
# for i in range(len(a)):
#     print(a[i],end=' ')
# output:
# [1, 2, 3, 4, 56, 76, 89, 90]
# 1 2 3 4 56 76 89 90
# 1 2 3 4 56 76 89 90


#2.difference between while and for?
#for loop is used to execute multiple statements whereas while loop also executes multiple statements when the
#statements are true only that means while loop checks the statement and after it'll executes.


#3.x=[1,2,4] access elements using index and without using index
#hint:using index-> use range fun in for
# x=[1,2,4]
# for i in range(len(x)):
#     print(x[i],end=' ')  #using index
# print()
# for i in x:
#     print(i,end=' ')     #without index
# output:
#  1 2 4
#  1 2 4


#4.Print even numbers b/w 1-10 write single line code
# x=list(range(0,11,2))
# print(x)
# output:[0, 2, 4, 6, 8, 10]
# print((list(range(0,11,2))))
# output:[0, 2, 4, 6, 8, 10]
# x=[i for i in range((10)) if i%2!=0]
# print(x)


#5.x=[1,5,6,8,9,7] print all even numbers and odd numbers from list
#x=[1,5,6,8,9,7]
# for i in x:
#     if(i%2==0):
#         print(i,end=' ')
# output: 6 8
# for i in x:
#     if(i%2!=0):
#         print(i,end=' ')
# output: 1 5 9 7


#6.wap to print 1-10 numbers by using while loop?
# 1-10
# i=1
# while(i<=10):
#     print(i,end=' ')
#     i=i+1
# output:
# 1 2 3 4 5 6 7 8 9 10
# i=1
# while(i<=10):
#     print(i,end=' ')
#     i=i+1


#7.What will be the output after the following statements?
# x=1
# y=4
# while x+y<10:
#     print(x*y,end=' ')
#     x+=1
#     y+=1
# output: 4



#8.What will be the output after the following statements?
# x,y=2,5
# while y-x<5:
#     print(x*y,end=' ')
#     x+=3
#     y+=4
# output: 10 45


# 9.What will be the output after the following statements?
# x='hello'
# for i in x:
#     print(i,end='')
#output: hello


# 10.What will be the output after the following statements?
# x={'z:1','y:2','z:3'}
# for i in x:
#     print(i,end=' ')
# output: z:1 y:2 z:3


#11.
# x={'x':1,'y':2,'z':3}
# for i,j in x.items():
#     print(i,j,end=' ')
# output:x 1 y 2 z 3


# 12.x=[1,2,3] o/p:[10,20,30] use for or while loop
# x=[1,2,3]
# for i in x:
#     print(i*10,end=' ') #using for loop
# x=[i*10 for i in [1,2,3]]
# print(x)

#output: 10 20 30


# 13.print below pattern
# *****
# *****
# *****
# for i in range(1,4):
#     print('*'*5,end='')
#     print()
# #output:
# *****
# *****
# *****


# 14.print below pattern
# *
# **
# *
# **
# *
# for i in range(1,6):
#     if i%2==0:
#         print('**')
#     else:
#         print('*')
# for i in range(1,6):
#     if i%2==0:
#         print('**')
#     else:
#         print('*')

# 15.Print below pattern
# x='python' take input from keyboard use input function
# p
# py
# pyt
# pyth
# pytho
# python
# x='python'
# for i in range(len(x)):
#   print(x[:i+1])
# x='sreedivya'
# for i in range(len(x)):
    # print(x[:i+1])
    # print(x[i:])

# function: function is a group of statements in a single unit.
# the main advantage of function is its reusability
# there are two types of functions are there.they are: inbuilt and user-defined functions
# function starts with def keyword in function
# built-in functions are:len(),max(),id(),type(),input(),print(),sorted(),eval(),pow(),math module()
# user-defined:functions developed by programmer are known as user-defined
# syntax:def_fun(args):
# def python():
# four types of functions are there:
# 1.without args return values
# 2.without args without return values
# 3.with args with return values
# 4.with args without return values
# def python():
#     print("a")
# python()
# def java():
#     x=20
#     y=30
#     return x+y
# print(java())

# def python(x,y):
#     # x=10
#     # y=20
#     print("x,y")
#     print(x+y)
# python(13,52)
# def python(a,b):
#     return a*b
# print(python(2,4))
# c=python(2,4)
# print(c)
#def add(a,b):
#     a=a+10
#     b=b+20
#     c=500
#     d=657
#     return a,b,c,d
# i,j,x,y=add(52,35)
# print(i)
# print(j)
# print(x)
# print(y)

#positional arguments:
#values which are directly assigned to the function arguments it provide arguments to the function call

#keyword argument:
#keywords argument is preceded by a parameter and the assignment operator,=
#keyword arguments can be linked to dictionaries in that map a value to a keyword
# def add(a,b,c,d):
#     a=a+12
#     c=c+5
#     print("a val:",a)
#     print("b val:",b)
#     print("c val:",c)
#     print("d val:",d)
# add(a=200,b=20,c=34,d=89)

#default arguments:
#default arguments are always right side of the function declaration
#if we pass any value to the argument it'll be printed if we don't pass any arguments then it'll take default arguments
# def add(a,b,c='python'):
#     print(a)
#     print(b)
#     print(c)
# add("java",3)
# add("java",34,20.5)

#variable length argument:
#variable length argument accepts n.no of arguments and return in tuple
#syntax: def_fun(*arg)
# def java(x,*y):
#     print(x,y)
# java(10,34,2,5,6,7,8889,799)
# keyword len argument:
# we can declare the keyword varaible length argument in (**variable_name) and the result in dictionary
# def sub(**d):
#     print(d)
# sub(a=20,b=39)
def divya(a):
    return a
a="the lazy dog ran after a butterfly"
k=divya(a[::-1])
print(k)

# sub()
# def java(**a):
#     return list(a.keys()),list(a.values())
# key,val=java(x=10,y=20,z=30,p=40)
# print(key,val)      ['x', 'y', 'z', 'p'] [10, 20, 30, 40]
# def add(x):
#     f=1
#     for i in range(1,x+1):
#         f=f*i
#     return f
# # x=eval(input("enter x val:"))
# x=7
# val=add(x)
# print('factorial of {} is:{}'.format(x,val))
# print('s{}:{}'.format(x,val))
# x="diVya kovI"
# def sree(a):
#     return a.lower(),a.upper(),a.swapcase()
# ram,b,u=sree(x)
# print(ram,b,u)
# y="python is good"
# def low(b):
#     b=b.lower()
#     return b[::-1]
# i=low(y)
# print(i)

# x=[10,20,30,40]
# def add(s):
#     s=s.insert(2,34)
#     return s
# k=add(x)
# print(x)

x=[1,2,3]
# def key(**a):
#     return a
# y=key(a=1,b=2,c=3)
# print(y)
#or
# def key(b):
#     out={}
#     keyval=['a','b','c']
#     out=dict(zip(keyval,b))
#     return out
# y=key(x)
# print(y)
# def divya(A):
#     print("hey",A, "how r u")
# divya('divi')
# def java(x,y):
#     return x*y
# result=java(12,13)
# print(result)
# def x(a):
#     if a%2==0:
#         print(a,"is even")
#     else:
#         print(a,"is not even")
# x(20)
# x(5)
# def x(a):
#     for i in a:
#         print(i)
# x(range(1,20))
# def fact(num):
#     result=1
#     while num>=1:
#         result=result*num
#         num-=1
#     return result
# for i in range(9):
#     print(i,':',fact(i))
def greet():
    print('hello')
    print('good morning')
def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d
result1,result2=add_sub(5,4)
print(result1,result2)

greet()
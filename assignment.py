#what is variable ? write variable rules.

#variable:
#variable is a named memory location which is useful to store the data
#syntax: Var_name = value
#Rules:
#variable name must start with alphabets (lower and upper) or with underscore but no special characters are allowed
#variable name cannot start with a number
#variable name can have alphanumeric characters and underscores
#variable names are case sensitive
#variable name should'nt be a keyword




#what is data type ? how many data types in python, write with examples?

#data type:
#data type represents the type of the data present inside the variable
#we no need to specify the type explicity to the variable
#data types are int,float,complex,bool,string,bytes,bytearray,range,list,tuple,set,frozen set, dictionary,none
#bytes,bytearray,complex,frozenset are rarely used data types


#int: whole numbers are called integers
# x=10
# print(x,(type(x)))
# output: 10 <class 'int'>


#float: numbers with decimal point
# y=20.3
# print("value of y:",y,type(y))
#output: value of y: 20.3 <class 'float'>


#complex: numbers with real and imaginary part
#a=2+6j
# print("value of a:",type (a),a)
# output: value of a: <class'complex'> (2+6j)


#bool: returns the value 'True or False'
# a=bool(2+6j)
# print(a,type(a))
#output: True <class 'bool'>

# a=bool(0.0)
# print(type(a),a)
# output: <class 'bool'> False


#string: characters are return in single quotes ('') or in duoble quotes ("")
# a='hello daddy'
# print(a,type(a))
# output: hello daddy <class 'str'>


#bytes: it should contain only integers and its range is between 0 to 255, and we can't change the byte values
# x=[0,2,3,5,7,254]   #0 to 255
# y=bytes(x)
# print(type(y),x)
# for i in y:
#     print(i,end='')
# output:<class 'bytes'> [0,2,3,5,7,254]
#        02357254
#in bytearray we can change the bytearray value by using index


#range: range generates the sequence of numbers
#if we don't specify thw starting index it will take '0' as default starting index and -1 in the ending
#syntax: range(starting index, ending index, stepping)
# a=range(7)
# for i in a:
#     print(i,end='')
# print()
# x='pYRTYthon is good'
# # print(x.casefold())
# y=(x.title())
# print(y)
# print(y.swapcase())
# x=[1,2,3,1,2,3]
# print(x.index(3,2))
# print(x)


# for i,j in enumerate(x):
#     print(i,j)
# x=range(0,6)
# for i in a:
#     print(i,end='')
# print()
# a=range(1,6,2)
# for i in a:
#     print(i,end='')
#output: 0123456
         # 0123456
         # 135
#what is keyword ? how to know how many keywords are there in current module?
#keyword:
# keywords are the reserved words in python
#keywords are case sensitive
#keywords can't be used as variable name,function name or any other identifiers
#To know how many keywords are there in current module execute the program by following
# import keyword
# print(keyword.kwlist)
# print(len(keyword.kwlist))
# output:
#['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif',
# 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or',
# 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
#35


#what is Typecasting? write an example to convert complex to string?
#Typecasting: Converting of one type of data type into another type is called type casting
#inbuilt data types
#integer, float, complex, bool, string
#complex to string:
#we can convert all types of datatypes into complex
#we can't convert string to complex if string contains only alphabets or alphanumerics
# x='123'
# print(complex(x))
#output: (123+0j)
# y='ab1h2$S'  #couldn't convert string to complex: 'ab1h2$S'
# print(complex(y))
# x="navyadivya" #couldn't convert string to complex
# print(complex(x))



#what is list, set, tuple, dictionary with examples?
#list: list is a collection of different types of data elements, which is mutable and is represented in []
#duplicates are allowed in list and has growable nature
#list index starts from'0' and ends with 'len of list-1'
# syntax: list_name=[]
# x=list()
# print(type(x))
#output:<class'list'>
# x=[1,2,3,9,8,7]
# print(x[0])
# output:1
# x=[200,35,74,95,500,26784]
# print(x[:-1])
# output:[200,35,74,95,500]
# print(x[1:6:3])
# output:[35,500]

#set:collection of unique elements and is return in {}
#duplicates are not allowed in set and there is no insertion order and it is mutable
#we can add n number of elements into set using add function
#syntax:set_name=set()
# x=set()
# print(type(x))
#output:<class'set'>
# x={1,2,3,4,1,2,4}
# print(x)
# output:{1,2,3,4} #duplicates are not allowed
# x.add(25)
# print(x)
# output:{1,2,3,4,25} #added element can be added anywhere in the set

#tuple:tuple is like list but we can't change the values in a tuple and is return in ()
#tuple is immutable and duplicates are allowed
#+ve index starts from '0' and -ve index starts from '-1' from backward direction
#syntax:tuple_name=tuple()
# x=2,3,4,5
# print(type(x),x)
# output:<class'tuple'> (2, 3, 4, 5)
# x=(100,200,300,400,500,600)
# print(x[2:-2])
# output:(300,400)
# a=(1,3,5,7,9,11,13,2,4,3,5,7)  #index,count
# print(a.index(3))
# print(a.index(5))
# output: 1
#         2

#dictionary: collection of key and value pairs is known as dictionary
#here duplicate keys are not allowed but values can be duplicated,only updated value is taken
#it is mutable and indexing and slicing are not applicable
#syntax:x={'key1':val1,'key2':val2}
#x={},is known as empty dictionary
# a={'x':99,'y':100}
# print(a)
#output:{'x': 99, 'y': 100}
# y={'p':10,'q':20,'p':"divya",'q':"navya"}
# print(y)
# print(y.values())
# print(y.keys())
# print(y['p'])
# print(y['q'])
#output:
# {'p': 'divya', 'q': 'navya'}
# dict_values(['divya', 'navya'])
# dict_keys(['p', 'q'])
# divya
# navya


#difference between list and set?
#"list" is ordered sequence of elements whereas "set" is unordered sequence of elements
#"list" allows duplicates whereas "set" doesn't allows duplicates
#indexing and slicing are applicable in "list"unlike "set"


# difference brtween set and tuple?
#"set" is mutable whereas "tuple" is immutable
#"set"is unordered and "tuple" is ordered
#indexing and slicing aren't applicable in "set" and are applicable in "tuple"
#in "set" duplicate eleemnts are not allowed but in "tuple" duplicate elements are allowed


#does duplicate keys are allowed in python?
#duplicate keys are not allowed in dictionary but duplicate values are allowed


#x=123.convert to string and find the len of the string
# x=123
# print(x)
# print(type(x))
# y=str(x)
# print(y)
# print(type(y))
# print(len(y))
#output:
# 123
# <class 'int'>
# 123
# <class 'str'>
# 3


#x={1},y={'A':100,'B':143} what is the difference between x and y?
# x={1}
# print(x)
# y={'A':100,'B':143}
# print(y)
# print(type(x),type(y))
#output:
# {1}
# {'A': 100, 'B': 143}
# <class 'set'> <class 'dict'>
#here the difference between x and y is 'x' is set and 'y' is dictionary

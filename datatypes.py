#data type represent the type of data present inside the varaiable
#there is no need to specify the type explicity to the variable
#int,str,bool,complex,float,bytes,bytearray,range,list,set,tuple,dictionary,frozenset,none are the data types
#whole numbers are known as integers
#decimal point values are known as float
#variable in "" are known as strings
#if the value is 1 it'll return true or if the value is 0 it'll return false are known as boolean type
#variable in the form of 1+3j i.e; real part and imaginary part are known as complex
# bytes shouild be return in list only and their values must be in range of 0 to 255
# and that list should only contains integers
# we cannot change the bytes value
# x=[1,34,234,255]
# y=bytes(x)
# print(y[0])
# print("type of y:",type(y))
# for i in y:
#     print(i,end='')
#     print()
# in bytearray we can change the value using index
# a=[2,4,3,1,65,56,245,255]
# x=bytearray(a)
# for i in x:
#     print("type of x",type(x))
# a[0]=23
# print(a[0])
# range:
# range generates the sequence of numbers
# if we won't specify the starting index then it'll take 0 as the default starting index
# stepping is allowed in range
# (ending index,starting index,stepping)
# ending index is len of the list-1
# x=range(3)
# for i in x:
#     print(i,end=' ')
#     print()
# x=range(0,23)
# for i in x:
#     print(i,end=' ')
#     print()
# x=range(23,2,-2)
# for i in x:
#     print(i,end=' ')

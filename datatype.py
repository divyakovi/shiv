#strings: string is a collection of characters either it may be written in " " or in ' '
# strings are immutable
# syntax:variable name='str' or "str"
# string index of strings is 0 and backward direction starting index is-1

# x='hello'
# print(type(x))
# y="hi"
# print(type(y))
#x="python"
# x[0]
# print(x[0])
# print(x[::2])
# print(x[-3::2])
# print(x[len(x)-1])
# print(x[:2])

# x=[1,2,3,4]
# print(x[0])
# x[0]=100
# print(x)
#a='python'
#print(a[::-1])
#to access string elements
#print(a[-1])
# print(type('''a''')) #multi line comment is not possible if its given only at one side
#print(a[:2])

#accessing elements using loop
#acessing elements directly without index
# for i in a:
#     print(i,end=' ')
# print()
# for i in range(len(a)):
#     print(a[i],end=' ')
# print()
# print(a)
# x="python"
# y=list(x)
# print(y)   #accessing element using index
# for i in range(len(y)):
#     if y[2]=='t':
#         y[2]='kk'
#         print(y[i],end=' ')
# x="".join(y)
# print(y)
#print(type(x))
# x=(1,2,3,4)
# for i in x:
#     print(i,end=' ')
# print(type(x))

# + * operators we can use in strings
# + is used to add two strings
#whereas * is used to multiply one string and one integer  and two strings can't be multiplied

x="python"
#y=2
# print(x+y)
# z="java"
# print(x+y+z)
# print(x*y)
# print(3*x[::-1])
# print(x*3)
# print(sorted(x,reverse=True))
#print(sorted(x,reverse=False))

# for i in range((len(x))):
#     print(x[:i+1])
# for i in range(len(x)):
#     for j in range(i+1):
#         print(x[j],end='')
#     print()
#x="12345"
# # for i in range(len(x)):
# #     print(x[:i+1])
# for i in range(len(x)):
#     for j in range(i+1):
#         print(x[j],end=' ')
#     print()
x='*****'
# for i in range(1,6):
#     if i%2==0:
#         print('123')
# for i in range(1,len(x)):
#     print(" "*(len(x)-i))
#     for j in range(1,i+1):
#         print('*',end='')
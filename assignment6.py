#1.Find the length of the string without using length function?
# x="pythonworld"
# c=0
# for i in x:
#     c=c+1
# print(c)
# x='pythonworld'
# c=0
# for i in x:
#     c=c+1
# print(c)
# o/p:11
#

#2.x=1A2B3C  o/p:123ABC
# x='absic485g36577fjbd'
# y=''
# z=''
# for i in x:
#     if i.isdigit():
#         y +=i
#     else:
#         i.isalpha()
#         z +=i
# print(y+z)
# o/p:123ABC
# x='absic485g36577fjbd'
# y=''
# z=''
# for i in x:
#     if i.isdigit():
#         y+=i
#     else:
#         i.isalpha()
#         z+=i
# print(y+z)

# #3.x=[1,0,0,1,0,1,0] o/p: 0000111 in string format
# x=[1,0,0,1,0,1,0]
# x.sort()
# print(x)
# y=[str(i) for i in x]
# a=str("".join(y))
# print(a)
# def f():
#     s="me too."
#     s='you eill win'
#     print(s);
# f();
# import re
# hand= open("doslect.txt")
# for line in hand:
#     line=line.rstrip()
#     x=re.findall('__',line)
#     if len(x)>0:
#         print(x)
# def clean(value)

#     ret =re.sub(r"^[A-Za-z0-9]"),"",value
#     return ret
# clean("what")
# o/p:0000111


# 4.x="hel$$lo#5#" o/p=hel$lo#5 remove only duplicates of each special characters alone
# x="hel$$lo#5#"
# y=list(x)
# out=[]
# for i in range(len(y)):
#     if x[i].isalpha():
#         out.append(x[i])
#     elif x[i].isnumeric():
#         if x[i] not in out:
#             out.append(x[i])
#     else:
#         if x[i] not in out:
#             out.append(x[i])
# print(out)
# z="".join(out)
# print(z)
#o/p:hel$lo#5


#5.print the maximum character which is occur in given string ex:HELLLOPQ o/p: maximum char in given string is L
# x='HELLLOPQ'
# y=set(x)
# print(y)
# max=0
# for i in y:
#     if x.count(i)>max:
#         max=x.count(i)
#         print("max char is {} and count is {}".format(i,max))
# o/p:max char is L and count is 3


#6.x="hello python java is good" count the number of words in given string and print output in below format
#o/p:hello5 python6 java4 is2 good4
# x="hello python java is good"
# y=x.split()
# for i in range(len(y)):
#     y[i]=y[i]+str(len(y[i]))
# print(y)
# o/p:['hello5', 'python6', 'java4', 'is2', 'good4']


#7.x='Hello javA Is Good' ...please make each word of first and last letter if it is upper make lower if it is lower
# make upper o/p:'hellO Java iS gooD
# x='Hello javA Is Good'
# y=x.split()
# print(y)
# for i in range(len(y)):
#     if y[i][0].isupper():
#         x=x.replace(y[i][0],y[i][0].lower())
#     if y[i][0].islower():
#         x=x.replace(y[i][0],y[i][0].upper())
#     if y[i][-1].isupper():
#         x = x.replace(y[i][-1], y[i][-1].lower())
#     if y[i][-1].islower():
#         x = x.replace(y[i][-1], y[i][-1].upper())
# print(x)
# o/p:hellO Java iS gOOD



#8.x='hello java'  o/p:'hello hello java java
# x='hello java'
# y=x.split()
# print(y)
# y=[i*2 for i in y]
# print(y)
# y=" ".join(y)
# print(y)
# o/p:hellohello javajava


#9.swap commas to dots and dots to commas
#input:14,625,498.002     o/p: 14.625.498,002
#x='14,625,498.002'
# x=x.replace('14,625,','14.625.').replace('498.002','498,002')
# print(x)
# o/p:14.625.498,002


#10.'12&&3AB$&+'      o/p:&&$&+ print only special characters from string
# x='12&&3AB$&+'
# num=''
# upper=''
# special=''
# for i in range(len(x)):
#     if(x[i].isdigit()):
#         num = num + x[i]
#     elif(x[i].isupper()):
#         upper = upper + x[i]
#     else:
#         special += x[i]
# print(special)
#o/p:&&$&+
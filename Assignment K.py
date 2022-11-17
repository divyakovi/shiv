#1.write a python program that returns a string sorted alphabetically by the first character of a string of words
# x=('red black white pink yellow')
# y=x.split()
# print(y)
# y.sort()
# for i in y:
#     print(i,end=' ')
#o/p:black pink red white yellow

#2.write a python program that takes a string and replaces characters with their respective numbers
# x='java IS Good'
# for i in x:
#     print(ord(i),end=' ')
# o/p:106 97 118 97 32 73 83 32 71 111 111 100

#3.write a program to find the largest and smallest words in a string
# x = " every contact leaves a trace says edmondlocard"
# x = x.split()
# out = 1
# temp = 0
# for i in x:
#     s = len(i)
#     if s < out:
#       out = s
#     elif s > temp:
#       temp = s
# for j in x:
#   k = len(j)
#   if k == out:
#     print ("smallest word is:",j)
#   if  k == temp:
#     print ("largest word is:",j)
# o/p:
# smallest word is: a
#  largest word is: edmondlocard


#4.write a program to print only the first repeated word in the string
# x=("ab",'abcd',"abc","abcd",'abc')
# a=0
# for i in range(0 , len(x) ):
#     if a==1:
#         break
#     for j in range(i+1 , len(x)):
#         if x[i]==x[j]:
#             print(x[i])
#             a=1
#             break
# if a==0:
#     print("nothing to print")

#5.write a program to write all the upper,lower,special,and numerics in the given string
# x="CODE error_404"
# upper, lower, num, special=0,0,0,0
# for i in range(len(x)):
#   if(x[i]>='A' and x[i]<='Z'):
#      upper+=1
#   elif(x[i]>='a' and x[i]<='z'):
#      lower+=1
#   elif(x[i]>='1' and x[i]<='9'):
#       num+=1
#   else:
#       special+=1
# print("Upper case letters: ",upper)
# print("Lower case letters: ",lower)
# print("numbers: ",num)
# print("Special characters: ",special)
# o/p:
# Upper case letters:  4
# Lower case letters:  5
# numbers:  2
# Special characters:  3

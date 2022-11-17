# a,b=10,a+30
# a=10
# b=a+30
# print(a,b)
# output:10 40


# a=20
# b=30
# a+=b #a=20+30=50
# b=a//b #50//30=1
# print(a,b)
# output: 50 1


# a,b=10,2
# print(a&b)
# print(a|b)
# print(a^b)
# print(a<<b)
# print(a>>b)
# print(~a)
# output:2
#        10
#        8
#        40
#        2
#       -11


# x=[1,2,5]
# print(x[-1])
# output: 5


#How to reverse the list without using reverse function(use slicing)?
# a=[1,2,3,4,5,6,7,8,9,10]
# print(a[::-1])
# print(a[::-1])
# output:[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


#x="python is good" check "h" is present or not in x?
# x="python is good"
# print("h" in x)  #membership operator
# output:True


# Difference between list, set, tuple?
# list,set are mutable whereas tuple is immutable
# list,tuple allows duplicates whereas set doesn't allows duplicates
# list,tuple are ordered hwereas set is unorderd
# indexing and slicing are applicable in list,tuple and aren't applicable in set


# how to find the address of variable?
#by using id() function we can find out the address of variable
#address of variable can be changed
# x=20
# print(id(x))
# x=20
# print(id(x))
#output:
#2169323782992
#2169323782352


# what is range and write an example?
# range: range generates the sequence of numbers
# if we don't specify the starting index it will take '0' as default index and -1 in the ending
# syntax: range(starting index,ending index,stepping)
# y=range(10)
# for i in y:
#     print(i,end='')
# print()
# y=range(0,10)
# for i in y:
#     print(i,end='8')
# print()
# y=range(1,8,3)
# for i in y:
#     print(i,end='')
# y=range(10)
# print(y)
# for i in y:
#     print(i,end=' ')
# output:
# 0123456789
# 08182838485868788898
# 147


# what is ternary and logical operator write an example?
# ternary operator:'if' condition is true first value will be considered,'else' condition is false second value will be
# considered
#x,y=8,9
# print(x)
# print(y)
# a=x if not(0) else 10
#print(a)
# if ((x<3 and y>6)):
#     print(x)
# else:
#     print(20,"divya")
# output:
# 8
# 9
# 8
# 20 divya
#logical operator: logical operators are operators which are used on conditional statements like true or false
#AND OR NOT are the logical operators
#AND: if first condition is false no need to check second condition
# if first condition is true need to check the second condition either true or false
# a=20
# b=15
# print(a<30 and b>20)      #first condition is true need to check second and second is false #false
# print(a>=20 and b<=15)    #both conditions are true #true
# print(a>32 and b>12)      #both conditions are false #false
# output:
# False
# True
# False
#OR: if both conditions are false then it will return false
# if any one of the condition or both the conditions are true then it will return true
# x=2
# y=1
# print(x<=0 or y>0)  #here first condition is false and second condition is true #true
# print(x>3 or y<0)   #both conditions are false # false
#output:
# True
# False
#NOT: if the variable is non zero it will return False and if the variable is zero it will return True
# a="divya"
# print(not a)
# print(not "divya")
# b=0
# print(not b)
# output:
# False
# False
# True
# a=20
# b=35
# print(not(a>=20 and b<40))
# print(not(a<10 or b>=40))
# output:
# False
# True


# 2.what is set comprehension? write an example?
# set comprehension: It is very easy and compact way of creating set objects from any iterable objects(like
# list,tuple,dictionary,range etc) based on some condition.
# example:
# x={i/2 for i in range(1,10) }
# print(x)
# o/p:{0.5, 1.0, 2.0, 2.5, 1.5, 3.0, 3.5, 4.0, 4.5}
#
#
# 3.x=[1,4,5,3,1,4] reverse the list and remove duplicates using set?
# x=[1,4,5,3,1,4]
# x.reverse()
# y=set(x)
# print(y)
# o/p:{1, 3, 4, 5}
#
# 4.Take two sets get unique values from set?
# x={10,20,30,40,50}
# y={40,50,60,70,30}
# print(x.union(y))
# o/p:{70, 40, 10, 50, 20, 60, 30}
#
#
# 5.how to concantinate two sets. write an example?
# we can concantinate two sets by using union() function
# x={10,20,'a',10.5,True}
# y={'python',30,50}
# print(x.union(y))
# o/p:{True, 50, 10.5, 20, 'a', 10, 'python', 30}
#
#
# 6.write a program to get common elements from two sets?
# x={9,8,7,6,5,4}
# y={4,5,6,8,7,9}
# print(x.intersection(y))
# o/p:{4, 5, 6, 7, 8, 9}
#
#
# 7.write an example for tuple comprehension?
# x=(i//i for i in range(1,5))
# print(x)
# o/p:<generator object <genexpr> at 0x000001A807F01EE0> (tuple comprehension is not possible i.e;genertaor comprehension)
#
#
# 8.x=[6,3,2,5,1] sort the list elements without using sort function? op:[1,2,3,5,6]
# x=[6,3,2,5,1]
# print(sorted(x))
# o/p:[1, 2, 3, 5, 6]
#
#
# 9.write a program to change tuple values using list?
# x=(10,20,30,'python','java')
# y=list(x)
# print(y)
# y[3]=30.4
# print(y)
#
#
# 10.print the multiplication table using loops input should be taken from keyboard?
# a=int(input("table:"))
# for i in range(1,11):
#     print(a,'*',i,'=',a*i)
#
#
#

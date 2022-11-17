# list:
# list is a collection of different type of data elements
# syntax:list_name[]
# list values are retuen in []
# list is mutable and it has growable nature
# we can access the list elements by using indx
# slicing and indexing are allowed in list
# duplicates are aslo allowed in list
# starting index of list is 0 called forward direction and ending index is -1 is called backward direction
# using append function we can add elemnts in list
# x=[1,2,3,4,5,6,7,8,9,11,23,34,45,54,56,6567]
# print(type(x))
# print(x)
# x=list()
# print(x)
# print(len(x))
# x.append(10)
# y=[]
# for i in range(1,6):
#     x=int(input("enter x val:"))
#     y.append(x)
# print(y)
# x=[10,20,30,40]
# print(x[3])
# print(x[2:4])
# print(x[::2])
# print(x[8::-1])
# x=[10,20,35,67,34,35,10,10]
# # x.append('hi')
# # print(x)
# # x.insert(1,'hello')
# # print(x)
# print(x.count(35))

# x.remove(10)
# x.remove(35)
# print(x)
# y=['pyth','on','java']
# x.extend(y)
# print(x)

# x=[10,20,30,40,50,78]
# y=[]
# for i in (x):
#     x=int(input("enter x val:"))
#     y.append(x)
# print(y)
#x=[10,20,30,40,50,78]
# print(x[-2::1])
# print(x[:100])
# x.append({'a':100,'b':'python'})
# x.append([22,78])
# print(x)
# print(len(x))
# print(x[7][0])
# print(x[6])
#o/p:
# [10, 20, 30, 40, 50, 78, {'a': 100, 'b': 'python'}, [22, 78]]
# 8
# 22
# {'a': 100, 'b': 'python'}
# x=[10,20,30,40,50,78]
# # x.insert(2,[{'a':100,'b':'python'}])
# # print(x)
# y=[10,20,30,40,50,78]
# (x.extend(y))
# print(x)
# x.remove(20)
# print(x)
x=[4,5,6,7,8,9]
# print(x[::-1])
# x.reverse()
# print(x)
# x.__reversed__()
# print(x)
# y=[]
# for i in x:
#     y.insert(0,i)
# print(y)
#y=[x[len(x)-i]]
# for i in range(1,len(x)+1):
#     y = [x[len(x) - i]]          #comprehension
#     print(y)
# x=[12,10,23,25,10,10,78]
#print(x.count(10))
# def functi(x,y):
#     count=0
#     for i in x:
#         if i==y:
#             count=count+1
#     return count
# x=[2,3,4,5,6,7,8,9,3,4,5,4,4,67,6,5,4]
# y=3
# print('{} has occured {} times'.format(x,functi(x,y)))

# x=[2,3,4,5,6,7,8,9,3,4,5,4,4,67,6,5,4]
# print(x.__getitem__(3))
# y={item:x.count(item) for item in x}
# (y.get('3'))
# print(y) o/p:{2: 1, 3: 2, 4: 5, 5: 3, 6: 2, 7: 1, 8: 1, 9: 1, 67: 1}
# x=[2,3,4,5]
# def div(a):
#     a=a.pop()
#     return a
# i=div(x)
# print(x)



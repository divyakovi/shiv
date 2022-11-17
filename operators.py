# import keyword
# print(len(keyword.kwlist))
# import sys
# print("python version")
# print(sys.version)
# print(sys.version_info)
#
# import datetime
# now=datetime.datetime.now()
# print(now)
# print(now.strftime("%d-%m-%y %H:%M:%S"))
#
# import math
# r=1.1
# print(math.pi*r**2)
# x=input("f  user name:")
# y=input("l user name:")
# print("hello" ,y+" " ,x)

# x=(input("enter data type:"))
# list=print(x.split(","))
# y=tuple(list)
# print(list)
# print(y)

#x=[1,2,3,4,53,4,5,12,2,1,23,4]
# y=set(x)
# print(y)
# y=[]
# for i in x:
#     if i not in y:
#         y.append(i)
# print(y)
# y=[]
# x=[y.append(i) for i in x if i not in y ]
# print(y)

# x=[(1,2),(3,-4),(5,6)]
# y=[a+b for (a,b) in x]
# print(y)

# y=[sum(i) for i in x]
# print(y)

# y=[]
# for i in x:
#     out=0
#     for j in i:
#         out+=j
#     y.append(out)
# print(y)

# for (a,b) in x:
#     print(a+b ,end=' ')

# x=(('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
# y=['white' in i for i in x]
# print(y)
# x=(10,20,40,5,60)
# for i in x:
#     print(i,end="")

# x=(('333', '33'), ('1416', '55'))
# y=tuple((int(i[0]), int(i[1])) for i in x)
# print(y)
# x=((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
# y=[sum(i)/len(i) for i in x]
# print(y)
import math
# x=(4, 3, 2, 2, -1, 18)
# # y=[math.pow(i*2) for i in x]
# # print(y)
# temp = list(x)
# for x in temp:
#     product = 1
#     product *= x
#     print(temp)
# x=input("enter name:")
# if x !='virat':
#     print("hey how r u !")
# else:
#     print("its virat kohli Divs")
# print("hello handsome!")


# for i in range(1,20):
#     if i%2==0:
#         print(i)
#     elif i%2!=0:
#         print(i)
# else:
#     print("oops")
# i=0;
# while False :
#  i=i+1;
#  print("Hello",i)
#  i=i+1

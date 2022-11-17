# iterative statements
# python supports only two iterative statements they are for and while
#for loop: if we want to execute multiple statemnts we use for loop
# x=range(1,11)
# # for i in x:
# #     print(i,end=' ')
# #
# for i in range(1,11,2):
#     print(i,end=' ')
# print()
# for i in range(1,11):
#     print(i,end='')
# x=list(range(1,11))
# print(x)
# for i in x:
#     print(i,end=' ')
# for i in range(len(x)):
#     print("index:",i,"ele:",x[i])
#     print(i,x[i])
# x=23
# if(x%2==0):
#     print("even")
# else:
#     print("odd")

x=[1,2,3,5,7,6,4,8,9,57,82,69,45,78,255,200026]
# for i in x:
#     print(i,end=' ')
# print()
# for i in range(len(x)):
#     print(x[i],end=' ')
# print()
# for i in x:
#     if i%2==0:
#         print(i)
# for i in range(len(x)):
#     if x[i]%2==0:
#         print(x[i])


#for else
# x=[12]
# for i in range(len(x)):
#     print(x[i],end='')
# else:
#     ("for executed successfully")

# for i in range(1,4):
#     print('*'*i,end=' ')
#     print()
# x='python'
# for i in x:
#     print(i,end=' ')
#     print()
# for i in range(len(x)):
#     print(x[i],end=' ')
#     print()
# x=int(input("enter x val:"))
# print(type(x))
# for i in range(x):
#      print('#'*2)
# x=[10,20,40,5]
# for i in range(0,4):
#     print(x[i],end='')
x='python'
for i in range(len(x)):
    print(x[i]*i)

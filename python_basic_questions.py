'''with continue statement'''
# i=0
# while i<6:
#     i=i+1
#     if i==4:
#         continue
#     print(i)
'''Adding elements to the list, using while loop'''
# my_list=[]
# i=0
# while i<5:
#     my_list.append(i)
#     i=i+1
# print(my_list)
'''Number series print'''
# i=10
# while i<=100:
#     print(i,end=" ")
#     i=i+10
'''sum of n natural numbers'''
# s=0
# i=0
# n=int(input("Enter your n. : "))
# while i<n+1:
#     s=s+i
#     i=i+1
# print("sum of",n,"natural numbers =",s)
'''factorial of number'''
# f=1
# i=1
# n=int(input("Enter your number: "))
# while i<n+1:
#     f=f*i
#     i=i+1
# print("Factorial of",n,"=",f)
'''fibonacci series'''
# n1=0
# n2=1
# i=0
# a=int(input("enter the terms up to which you want series: "))
# while i<a:
#     print(n1,end="")
#     n3=n1+n2
#     n1=n2
#     n2=n3
#     i=i+1
'''Fibonacci series using for loop'''
# n1=0
# n2=1
# n=int(input("enter number of terms: "))
# for i in range(0,n):
#     print(n1,end="")
#     n3=n1+n2
#     n1=n2
#     n2=n3
'''10 numbers from user and to find their average-'''
# i=0
# my_list=[]
# while i<10:
#     n=int(input("Enter your number: "))
#     i=i+1
#     my_list.append(n)
# average=sum(my_list)/10
# print("Average of 10 input numbers=",average)
'''infinte loop, which breaks with q input from the user, asking input numbers fro keyboard
to find the average and product of the numbers'''
# sum=0
# while True:
#     n=input("Enter your number: ")
#     if n=="q":
#         break
#     sum=sum+int(n)
# print(sum)
'''Nested While Loops'''
# l=[[1,2,3,4],[5,6,7,8],["a","b"],(1,2,"abhishek")]
# i=0
# while i<len(l):
#     print(l[i])
#     j=0
#     while j<len(l[i]):
#         print(l[i][j])
#         j=j+1
#     i=i+1
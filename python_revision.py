'''prime number or not'''
# n=int(input("enter your number: "))
# for i in range(2,n):
#     if n==2:
#         print(n,"is prime")
#     elif n%i==0:
#         print(n,"is not prime")
#         break
#     else:
#         print(n,"is prime")
#         break
'''lcm of two numbers'''
# def lcm(n1,n2):
#     if n1>n2:
#         greater=n1
#     else:
#         greater=n2
#     while True:
#         if (greater % n1==0) and (greater % n2 ==0):
#             lcm=greater
#             break
#         greater+=1
#     return lcm
# print(lcm(9,6))
'''hcf of two numbers'''
# def hcf(n1,n2):
#     if n1>n2:
#         smaller=n2
#     else:
#         smaller=n1
#     for i in range(1,smaller+1):
#         if (n1%i==0) and (n2%i==0):
#             hcf=i
#     return hcf
# print(hcf(3,4))
'''star patterns-----
1. right triangle'''
# n=int(input("enter the number of lines: "))
# for i in range(0,n):
#     for j in range(0,i+1):
#         print("*",end="")
#     print()
'''2.reverse right triangle'''
# n=int(input("enter the number of lines: "))
# for i in range(0,n):
#     for j in range(i,n):
#         print("*",end="")
#     print()
'''3. another star pattern'''
# n=int(input("enter no. of lines: "))
# for i in range(0,n):
#     for j in range(0,i):
#         print(" ",end="")
#     for j in range(i,n):
#         print("*",end="")
#     print()
'''4. one more star pattern'''
# n=int(input("enter the number of lines: "))
# for i in range(0,n):
#     for j in range(i,n):
#         print(" ",end="")
#     for j in range(0,i+1):
#         print("*",end="")
#     print()
'''5. pyramid star'''
# n=int(input("enter no. of lines: "))
# for i in range(0,n):
#     for j in range(i,n):
#         print(" ",end="")
#     for j in range(0,i):
#         print("*",end="")
#     for j in range(0,i+1):
#         print("*",end="")
#     print()
'''6. inverse pyramid'''
# n=int(input("enter no. of lines: "))
# for i in range(0,n):
#     for j in range(0,i+1):
#         print(" ",end="")
#     for j in range(i,n-1):
#         print("*",end="")
#     for j in range(i,n):
#         print("*",end="")
#     print()
'''7. diamond pattern'''
# n=int(input("enter no. of lines: "))
# for i in range(0,n):
#     for j in range(i,n):
#         print(" ",end="")
#     for j in range(0,i-1):
#         print("*",end="")
#     for j in range(0,i):
#         print("*",end="")
#     print()
# for i in range(0,n):
#     for j in range(0,i):
#         print(" ",end="")
#     for j in range(i,n-1):
#         print("*",end="")
#     for j in range(i,n):
#         print("*",end="")
#     print()
'''8. No. pattern'''
# n=int(input("enter your number: "))
# p=1
# for i in range(0,n):
#     for j in range(0,i+1):
#         print(p,end="")
#     p=p+1
#     print()
'''9. another number pattern'''
# n=int(input("enter your number: "))
# for i in range(0,n):
#     p=0
#     for j in range(0,i+1):
#         print(p,end="")
#         p=p+1
#     print()
'''Square Pattern'''
# n=int(input("enter no. of lines: "))
# for i in range(0,n):
#     for j in range(0,n):
#         print("* ",end="")
#     print()
" Plus Pattern"
# n=5
# for i in range(n):
#     for j in range(n):
#         if (i==n//2 or j==n//2):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
'''cross pattern'''
# n=5
# for i in range(n):
#     for j in range(n):
#         if (i==j or i+j==n-1):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
''' two bars apart'''
# n=5
# for i in range(n):
#     for j in range(n):
#         if (j==0 or j==n-1):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
''' empty square'''
# n=5
# for i in range(n):
#     for j in range(n):
#         if (i==0 or i==n-1 or j==0 or j==n-1):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
''' empty right triangle'''
# n=int(input("enter the number of lines: "))
# for i in range(0,n):
#     for j in range(0,i+1):
#         if i==n-1 or j==i or j==0:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
''' empty reverse triangle'''
# n=int(input("enter the number of lines: "))
# for i in range(0,n):
#     for j in range(i,n):
#         if i==0 or j==i or j==n-1: '''here for i range is i to n-1 so i==0 and j==i then j==n-1'''
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
''' enumerate function in lists'''
# l1=["a","b","c","d","e"]
# for index,elements in enumerate(l1):
#     print(index,elements)
########################################
# l1=["a","b","c","d","e"]
# for i,elements in enumerate(l1,100):
#     print(i,elements)
########################################
# n=5
# for i in range(5):
#     for j in range(5):
#         if j==0 or i==4 or i==j:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
#########################################
n=5
for i in range(5):
    for j in range(5):
        if i==0 or j==4 or i==j:
            print("*",end="")
        else:
            print(" ",end="")
    print()
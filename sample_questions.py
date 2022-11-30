##Q-1
'''user will input 3 ages. Find the oldest one.'''
# a=int(input("enter your age: "))
# b=int(input("enter your age: "))
# c=int(input("enter your age: "))
# if a>b:
#     g1=a
# else:
#     g1=b
# if g1>c:
#     print(g1,"is the greatest age")
# else:
#     print(c,"is the greatest age")
#####################################
'''user input 2 numbers, swap them'''
# a=int(input("enter your number: "))
# b=int(input("enter your number: "))
# a,b=b,a
# print(a,b)
'''sum of three digits by user'''
# a=int(input("enter your number: "))
# b=int(input("enter your number: "))
# c=int(input("enter yur number: "))
# sum=a+b+c
# print("sum of three numbers is",sum)
'''Palindrome number'''
# n=555
# t=n
# rev=0
# while t>0:
#     rem=t%10
#     rev=rev*10+rem
#     t=t//10
# if rev==n:
#     print("yes")
# else:
#     print("no")
#######################################
# n=input("enter number: ")
# a=list(n)
# a.reverse()
# print(a)
# b=""
# b=b.join(a)
# if b==n:
#     print("yes")
# else:
#     print("no")
'''n is even or not'''
# n=int(input("enter number: "))
# if n%2==0:
#     print(n,"is even")
# else:
#     print(n,"is odd")
'''profit loss determination'''
# n1=int(input("enter CP: "))
# n2=int(input("enter SP: "))
# if (n1-n2)>0:
#     print("loss")
# else:
#     print("profit")
'''triangle formed or not'''
# n1=int(input("enter angle1: "))
# n2=int(input("enter angle2: "))
# n3=int(input("enter angle3: "))
# if (n1+n2+n3)==180:
#     print("they can form a triangle")
# else:
#     print("they cant form a triangle")
'''multiply 2 numbers wihtout * operator'''
# n1=int(input("enter number1: "))
# n2=int(input("enter number2: "))
# i=0
# prod=0
# while i<n2:
#     prod=prod+n1
#     i=i+1
# print(prod)
'''fibonacci series first 20 terms'''
# n=int(input("enter no. of terms: "))
# n1=0
# n2=1
# for i in range(0,n):
#     print(n1,end=" ")
#     n3=n1+n2
#     n1=n2
#     n2=n3
''' finding average of numbers to be entered by user input and end only when 0 is entered--'''
# my_list=[]
# while True:
#     n1=int(input("enter number: "))
#     my_list.append(n1)
#     if n1==0:
#         break
# avg=sum(my_list)/(len(my_list)-1)
# print("average of numbers",avg)
'''length of given string without using len() function'''
# a="Abhishek"
# ind=a.find(a[-1])
# print(ind)
# len=ind+1
# print("length of string is",len)
'''username= abhi.einew1@gmail.com, extract abhi.einew1 from it'''
# email="abhi.einew1@gmail.com"
# username=email.rstrip("@gmail.com")
# print(username)
'''checking for string pallindrome'''
# a=input("enter a string: ")
# if a[::-1]==a:
#     print("yes",a,"is palindrome")
# else:
#     print("no",a,"is not palindrome")
'''dupicates removing from list'''
# l1=[1,1,1,2,2,2,3,4,5,6]
# s1=set(l1)
# l2=list(s1)
# print(l2)
'''max element in a list without using max function'''
# l1=[4,6,2,3,98,100,23]
# from functools import reduce
# a=lambda x,y :x if x>y else y
# print(reduce(a,l1))
##########################
# l1=[4,6,2,3,98,100,23,9999,2,4,5,6]
# max=l1[0]
# for i in l1:
#     if i>max:
#         max=i
# print(max)
# l1=[4,6,2,3,198,100,23]
# l1.sort()
# print(l1[-1])
''' reversing a string message'''
# a="hello how are you"
# l=a.split()
# l.reverse()
# b=" "
# c=b.join(l)
# print(c)
'''sorting a list in ascending order'''
# l1=[4,6,2,3,98,100,23]
# l2=[]
# while l1:
#     min=l1[0]
#     for i in l1:
#         if i<min:
#             min=i
#     l2.append(min)
#     l1.remove(min)
# print(l2)
'''string length with counter'''
# a='ajsjnsnbndfbkndbdfbjdfnn'
# c=0
# for i in a:
#     c=c+1
# print(c)
# print(len(a))
''' Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.'''
# for i in range(2000,3201):
#     if i%7==0 and i%5!=0:
#         print(i,end=",")
''' With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}'''
# n=int(input("enter number: "))
# d=dict()
# for i in range(0,n+1):
#     d[i]=i*i
# print(d)
'''Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')'''
# n=input('enter sequence: ')
# l1=n.split(',')
# t=tuple(l1)
# print(l1)
# print(t)
''' Question:
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world'''
# n=input("enter asequence: ")
# l=n.split()
# s=set(l)
# l=list(s)
# l.sort()
# print(" ".join(l))
'''Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3'''
# n=input("enter sequence: ")
# c=0
# d=0
# for i in n:
#     if i.isdigit():
#        c=c+1
#     elif i.isalpha():
#         d=d+1
#     else:
#         pass
# print("digits:",c)
# print("letters:",d)
'''Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9'''
# n=input("enter sequence: ")
# c=0
# d=0
# for i in n:
#     if i.isupper():
#         c=c+1
#     elif i.islower():
#         d=d+1
#     else:
#         pass
# print("upper case:",c)
# print("lower case:",d)
'''Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9'''
n=input("enter: ")
l=n.split(',')
l=[int(x) for x in l]
l=[x for x in l if x%2 !=0]
print(l)
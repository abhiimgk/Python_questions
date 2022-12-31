#1. solution --------
num=int(input("enter thenumber for square: "))
square=num**2
print(f"square of {num}:{square}")

#2.solution--------
n=input("enter your character: ")
x=n.lower()
if x=="a" or x=="i" or x=="e" or x=="o" or x=="u":
	print(f"{n} is a vowel")
else:
	print(f"{n} is a consonant") 

#3. solution-------
a=input("enter your string : ")
vowels=0
consonant=0
for i in a:
	if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
		vowels =vowels+1
	else:
		consonant=consonant+1
print(f" number of vowles are {vowels}.")
print(f"number of consonants are {consonant}.")

#4. Solution ---------
st= {"hello",15.89,55,89,100}
st.add("Abhishek")
st.add(105)
st.add(True)
st.add(False)
st.add("abhishek")
print(st)

#5. Solution------------
sum=0
#list of first 10 even number
l1=[2,4,6,8,10,12,14,16,18,20]
for i in l1:
	sum=sum+i
print(f"sum of first 10 even numbers ={sum}.")
###################################

sum=0
for i in range(1,21):
	if i%2==0:
		sum=sum+i
print(f" Sum of first 10 even numbers={sum}")

#6. Solution --------
even_list=[]
while True:
	a=int(input(f" Enter even number: "))
	if a%2==0:
		even_list.append(a)
	else:
		print("input only even numbers")
	if len(even_list)==10:
		break
print(even_list)

#7. Solution --------
Ls=[[2,6,8],(5,6,"hello",14.89)]
for i in Ls:
	if type(i)==list:
		for j in i:
			print(j)
	elif type(i)==tuple:
		for j in i:
			print(j)
			
#8.Solution ----------
'''remove() and discard() both removes specified element in the arguments. Only difference is that if 
element is not present in given data type, remove() will raise an error, 
while discard() will not cause error.'''

#9. Solution ---------
l1=[1,2,3,4,5,6]
l2=[3,4,8,9,10]
for i in l1:
	if i in l2:
		print(i)
#---#-#----#---------##
l1=[1,2,3,4,5]
l2=[6,7,8,1 ,2]
print( l1 in l2)
print(l1 not in l2)
		

#10. Solution -------
import numpy as np
a=np.arange(1,10)
print(a[0::2])
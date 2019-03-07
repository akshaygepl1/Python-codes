#Written by :- Sachin B M

#Program to find the factorial of given numbers using recursive function

#No. of elements to be entered
z=int(input("No. of elements in list: "))

#Creating a list 
n=[]

#Entering the elements by user
#Entering the the elements in the given range
for i in range(z):
	x=input("Enter the elements: ")
	y=int(x)
	n.append(y)

#Printing the given elements one by one
for l in range (len(n)):
	print("Entered element is: ",n[l])

#Function to find the factorial of given elements
def fact(n):
	if(n<1):
		return 1
	else:
		return n*fact(n-1)
m=[fact(p) for p in n]

#Printing the factorial of given elements one by one
for k in range (len(m)):
	print("Factorial of given element is: ",m[k])


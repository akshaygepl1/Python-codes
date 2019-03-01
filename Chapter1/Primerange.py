# Prime numbers within the given range

# take input from the user
n = int(input("Accept the first number"))
n1 = int(input("Enter the second number"))


# prime numbers are greater than 1
print("Prime numbers between",n,"and",n1,"are:")

for num in range(n,n1 + 1):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
            
            

# Factorial of the given numbers number
n = int(input("Enter the number for which the factorial has to be found"))
fact = 1
if n == 0:
    print("Factorial of ",n," is 1")
else:
   for i in range(1,n+1):
        fact *= i
print(fact,end=" ")


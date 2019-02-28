# Fibonacci series to display first n number

n = int(input("Enter the number to display first n number "))

n1=0
n2=1
print("Fibonacci series of first n number is: ")
while n!=0:
    print(n1, end=" ")
    nth = n1+n2
    n1=n2
    n2 = nth
    n-=1
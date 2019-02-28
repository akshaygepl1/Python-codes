# Prime numbers within the given range

n = int(input("Accept the first number"))
n1 = int(input("Enter the second number"))

for i in range(n,n1):
    if i % 2 == 0 or i == 1:
        print(i," is not prime number")
    else :
        print(i ,"Is prime number")
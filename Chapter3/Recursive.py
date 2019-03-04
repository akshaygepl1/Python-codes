# Factorial of a number by using recursive function

Input = int(input("Enter the number"))

def fact(n):
    if n < 1:
        return 1
    else:
        return n * fact(n-1)

print(fact(Input))

l1 = [int(x) for x in input("Enter values").split()]
l2 = [fact(y) for y in l1]

print(l1)
print(l2)
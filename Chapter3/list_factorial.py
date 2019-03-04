# factorial of list values

def fact(n):
    if n < 1:
        return 1
    else:
        return n * fact(n-1)



l1 = [int(x) for x in input("Enter values by providing space").split()]
l2 = [fact(y) for y in l1]

print(l1)
print(l2)
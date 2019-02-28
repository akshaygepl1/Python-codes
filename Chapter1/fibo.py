# Prints fibonacci numbers of max number

n = int(input("Enter the number for which fibonacci series is displayed : "))

n1 = 0
n2 = 1
ctr = 0
if n == 0 :
    print("The fibonacci of ",n1, " invalid")
elif n == 1:
    print("The fibonacci series of 1 is : ", n1)
else:
    print ("fibonacci series of ", n, " is")
    while n1<= n :
        print(n1)
        temp = n1+n2
        n1 = n2
        n2 = temp
        #ctr +=1

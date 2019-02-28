# 2.Find how many times a digit occurs in a given number
y = int(input("Enter the number"))
z = int(input("Enter the digit to be searched"))
i = 0

while(y!=0):
    q = y%10
    print(q)
    y = y//10
    if q == z :
        i += 1

print("Digit occured",i)
# 1. count number of digit in a given number
count = 0
x = int(input("Enter the digit to be counted"))
while x > 0:
    count = count + 1
    x = x//10
print(count)


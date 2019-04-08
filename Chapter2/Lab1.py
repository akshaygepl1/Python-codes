# Input  a sentence and display the longest word

User_Intput = input("Enter a sentence")

Longest = ""
Length = 0

List_Of_Words = [x for x in User_Intput.split()]

print(List_Of_Words)

for i in List_Of_Words:
    if(len(i)>Length):
        Longest = i

print(Longest)
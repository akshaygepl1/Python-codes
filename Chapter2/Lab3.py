# DISPLAY ALL THE WORDS THAT ARE CONTAINED IN A SENTENCE. WORDS THAT COME MULTIPLE TIMES  SHOULD BE DISPLAYED ONLY ONCE.

User_Input= input("Enter a Sentence")

List_Of_Words = [x.lower() for x in User_Input.split()]

S1 = set(List_Of_Words)

print(S1)
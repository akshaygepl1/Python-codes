# Get a list of words with their count in a sentence .
# The word should be in a sorted order alphabetically.Word should not be repeated.
# Assume space as separator for words.

User_input = input("Enter the sentence on which the operation will be performed :")
temp = list(set(User_input.split()))
t1 = temp
t1.sort()
print(t1)


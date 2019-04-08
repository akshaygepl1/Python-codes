# Input  sentence and input word. You have find out  how many time a word occurred in the sentence.

# Take input Sentence from the user
User_Input = input("Enter a sentence")
# Take word to be counted
Word_To_Search = input("Enter word to be counted")

List_Of_Word = [x for x in User_Input.split()]

print("The word ", Word_To_Search, "has occurred :",List_Of_Word.count(Word_To_Search))

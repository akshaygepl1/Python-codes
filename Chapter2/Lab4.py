#You wish to display only those words from the sentence that do not occur in a set of excluded words(eg. this,and,is,not,etc).
# The set of excluded words would be maintened in your code,and the sentence is input from the keyboard.
# You have to display all words that do not exist in this set, and you have to take care that multiple occuring words are displayed only once
user_input=input("Enter a sentence: ")
print(user_input)
excluded_words=["this","and","is","not"]
print(excluded_words)
b=user_input.split()
print(b)
c=set(b)
d=set(excluded_words)
e=c-d
r=list(e)
print(r)

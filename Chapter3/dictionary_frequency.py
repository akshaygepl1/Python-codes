sentence = "this is the textfile, and it is used to take words and count"

# split the sentence into words.
# iterate thorugh every word

ls = []
ls1 = []
for i in sentence.split():

    word_count = sentence.count(i)  # Pythons count function, count()
    ls.append((i,word_count))
    if(word_count > 1):
        ls1.append((i,word_count))


dict_ = dict(ls)

ls.sort()
print (dict_)
print(ls)
print(ls1)
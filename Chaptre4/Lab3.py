
# Creating a set from the ignore.txt

fr = open("ignore.txt","r")

L = fr.read().split()
fr.close()
ls =[]
fo = open("article.txt", "r")
L1 =  fo.read().split()
Total_words =len(L1)
print(Total_words)
#sorted(L1)


def check_ignore_Words(a):

    if a not in L:
        return True


L4 = {x:L1.count(x) for x in filter(check_ignore_Words, L1)}
print(L4)

#print(list(L4.keys()))

def check_Density(q):

    return round((q/Total_words)*100,4)


L5 = list(L4.values())
List_of_words = list(L4.keys())

L6 = [check_Density(x) for x in L5]
L7 = [z for z in zip(L5,L6)]

print(L6)
print(L7)
d2 = dict(zip(List_of_words,L7))
print(d2)



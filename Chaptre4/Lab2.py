# Lab Exercise 2 Need Book1.csv file
import csv

reader = csv.reader(open("Book1.csv"))
d={}
for row in reader:
    d[row[0]] = row[1:]
print (d)


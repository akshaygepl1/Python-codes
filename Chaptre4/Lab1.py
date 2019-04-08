# Reading file for temperature data, file consist one data temperature per line
# Temperature_data file has to be used to execute the program

fr = open("temperature_data", "r")

# Through comprehension we loaded contents of file to the list L
L = [ float(x) for x in fr.read().split()]
print(L)

# Implemented filter and lambda functions to achieve the condition specified
L1 = [ float(x) for x in filter(lambda x: x > 25, L)]
print(L1)


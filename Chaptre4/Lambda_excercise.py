# Input list
L1 = [1,2,3,8,6,7,11]

# Comprehension method with filter and Lambda implementation
L=[x for x in filter(lambda x: x%2 == 0, L1)]

# Print Output result
print(L)
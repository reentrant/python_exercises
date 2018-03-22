
## List Operations: List Addition and Lenght

# append mutates the list object
# + concatenates and creates a new object
# len() it works for a collection of things

# What is the value of len(p) after running:
p = [1,2]
p.append(3)
p = p + [4,5]
print len(p)

# What is the value of len(p) after running:
p = [1,2]
q = [3,4]
p.append(q)
print len(p)

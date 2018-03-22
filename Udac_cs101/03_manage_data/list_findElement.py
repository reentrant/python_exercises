'''

@author: jruiz
'''
# Define a procedure, find_element_using_a_while,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.

def find_element_using_a_while(p,t):
    i =0
    while i < len(p):
        if t == p[i]:
            return i
        i += 1
    return -1        

def find_element_using_a_for(p,t):
    i=0
    for e in p:
        if e == t:
            return i
        i = i + 1
    return -1

# Define a procedure, find_element,
# using index that takes as its
# inputs a list and a value of any
# type, and returns the index of
# the first element in the input
# list that matches the value.

# If there is no matching element,
# return -1.

def find_element(p,v):
    if v not in p:
        return -1
    else:
        return p.index(v)


print find_element_using_a_while([1,2,3],3)
print find_element_using_a_for([1,2,3],3)
print find_element([1,2,3],3)

print find_element_using_a_while(['alpha','beta'],'gamma')
print find_element_using_a_for(['alpha','beta'],'gamma')

print find_element(['alpha','beta'],'gamma')
#>>> -1

print 

p = [0,1,2]
print "<value> in <list>"
print 2 in p
print 3 in p
print "<value> not in <list> == not <value> in <list>"
print 2 not in p
print not 2 in p
print 3 not in p
print not 3 in p
print "<list>.index(<value>)"
print p.index(1)
print p.index(3)



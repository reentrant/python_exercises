
'''
Mutation modifies the existing object.
When we really see the difference is when we introduce
a new variable
'''


## Strings

s = 'Hello'
print s
print
s = 'Yello'  ## A new string is created
print 'Now "s" refers to: '
print s
print
s = s + 'w'  ## A new string is created
print 'Now "s" refers to: '
print s
print
t = s
s = s + 'ish'

print s
print

print t
print



## Lists

p = ['H','o','l','a'] ## Create a List
print p
print
p[0] = 'b'	      ## No new list is created
print p
print 

q = p
q[2] = 't'
print q
print 

print p
print 

'''
NOTE: Once that one object is mutable then we have
to worry about other variables that refer to the 
same object!!!
'''





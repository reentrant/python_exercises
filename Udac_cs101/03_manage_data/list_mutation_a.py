
## List vs Strings

## Strings

s = 'Hello'
print s

s = 'Yello'  ## A new string is created

print 'Now "s" refers to: '
print s
s = s + 'w'  ## A new string is created
print 'Now "s" refers to: '
print s

## Lists

p = ['H','o','l','a'] ## Create a List
print p
p[0] = 'Z'	      ## No new list is created
print p

s[0] = 'M'
print s		## NOTE: s is immutable...!!!




'''
# We defined:
stooges = ['Moe','Larry','Curly']
print stooges
# but in some Stooges films, Curly was
# replaced by Shemp.

# Write one line of code that changes
# the value of stooges to be:
#['Moe','Larry','Shemp']
# but does not create a new List
# object.


stooges[2]='Shemp' ## The solution uses mutation
print stooges
'''






#Aliasing:
# Mutable objects
#   List Of Strings:

p = ['H','e','l','l','o'];
print p
print len(p)
q =p;# It does not create a new list object
print q
print len(q)
p[0]='Y';
print q

p[4] = '!'; 
print q

# We defined:

stooges = ['Moe','Larry','Curly']

# but in some Stooges films, Curly was
# replaced by Shemp.

# Write one line of code that changes
# the value of stooges to be:
stooges[2]='Shemp'
print stooges
print len(stooges)
#['Moe','Larry','Shemp']

# but does not create a new List
# object.


# Now,
# Define a procedure, replace_spy,
# that takes as its input a list of
# three numbers, and modifies the
# value of the third element in the
# input list to be one more than its
# previous value.

spy = [0,0,7]


def replace_spy(aList):
    aList[2] = 1+ aList[2]
    #No need to return aList

    

# In the test below, the first line calls your 
# procedure which will change spy, and the 
# second checks you have changed it.
# Uncomment the top two lines below.

replace_spy(spy)
print spy
#>>> [0,0,8]

#We have a list p to begin with, and then we call a procedure with 
#input p.
# After the procedure is completed, the value of p is she same as the one we
# started with?
def procedure(p):
    p = p + [1]# Creates a new list
    print "Within procedure: "
    print p


print p
procedure(p)
print "Lets see the original list: "
print p

# Inmutable objects

s = 'Hello';
s[0] = 'y';
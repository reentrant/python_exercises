
# 2 GOLD STARS

# Define a procedure, print_multiplication_table,
# that takes as input a positive whole number, and prints out a multiplication,
# table showing all the whole number multiplications up to and including the
# input number. The order in which the equations are printed matters.

# Hint: You can not add an integer and a string, but in homework 1.9
# you came across a method, str, for turning an integer into a string.

def print_multiplication_table(n):
    i,j=0,0
    while i<n:
        i = i+1
        while j<n:
            j = j+1
            print str(i)+ '*'+ str(j)+ '= '+ str(i*j)
        j = 0

print_multiplication_table(2)
#>>> 1 * 1 = 1
#>>> 1 * 2 = 2
#>>> 2 * 1 = 2
#>>> 2 * 2 = 4

print_multiplication_table(3)
#>>> 1 * 1 = 1
#>>> 1 * 2 = 2
#>>> 1 * 3 = 3
#>>> 2 * 1 = 2
#>>> 2 * 2 = 4
#>>> 2 * 3 = 6
#>>> 3 * 1 = 3
#>>> 3 * 2 = 6
#>>> 3 * 3 = 9




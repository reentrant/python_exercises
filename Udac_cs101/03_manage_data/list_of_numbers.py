'''

@author: jruiz
'''
# Define a procedure, sum_list,
# that takes as its input a
# list of numbers, and returns
# the sum of all the elements in
# the input list.

def sum_list(p):
    my_sum =0
    for e in p:
        my_sum = my_sum + e
        print e
    return my_sum
        


print sum_list([1, 7, 4])
#>>> 12

print sum_list([9, 4, 10])
#>>> 23

print sum_list([44, 14, 76])
#>>> 134
# Define a procedure, product_list,
# that takes as input a list of numbers,
# and returns a number that is
# the result of multiplying all
# those numbers together.

def product_list(p):
    
    if p:
        product = 1
    else:
        product = 0
    
    for e in p:
        product *= e
    return product

print
print "Product list"
print product_list([9])
#>>> 9

print product_list([1,2,3,4])
#>>> 24

print product_list([])
#>>> 1

# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

def greatest(p):
    biggest = 0
    
    for e in p:
        if e > biggest:
            biggest = e        
    return biggest

print
print "Greatest: "
print greatest([4,23,1])
#>>> 23
print greatest([])
#>>> 0
print

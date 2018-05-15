'''
Created on 09/05/2018

@author: jruiz

Data Structures and Loops: Sets

'''
 
def remove_duplicates(lst):
    '''# Define the remove_duplicates function'''
    new_lst = []
    for e in lst:
        if e in new_lst:
            continue
        else:
            new_lst.append(e)
    return new_lst


def buiding_a_set(sqr_set, limit):
    n = 1
    while n * n < limit:
        sqr_set.add(n ** 2)
        n += 1
    return sqr_set

lst = [1,1,2,2,3,3]
print("Original list: ", lst)
    
print(remove_duplicates(lst))

print('Set: ', end='')
print(set(lst))

squares = set()
# TODO: Populate squares with the set of all integers less than 2000 that are
#        square numbers.
print(buiding_a_set(squares, 2000))




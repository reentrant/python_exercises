#!/usr/bin/python -tt
# Source:
# LEARNING TO PROGRAM WITH PYTHON
# Richard L. Halterman
"""
Example: Using "is" keyword
"""

import random

def create_random_list(n):
    '''
    Creates a random list of integers
    '''
    return [random.randrange(100) for _ in range(n)]


# Define a main() 
def main():
    try:
        #===========================================================================
        # The Python keyword is tests whether two variables refer to the exact 
        # same object, not just if they are equal. For example:
        #===========================================================================
        list_1 = [1, 2, 3]
        list_2 = [1, 2, 3]
        print("list_1 == list_2? %s" % (list_1 == list_2))
        print("list_1 is list_2? %s" % (list_1 is list_2))
        is_alias = lambda x,y: x is y
        input_size = int(input("Enter list size: "))
        random_list = create_random_list(input_size)
        print(random_list)
        alias = random_list
        alias[0] = 55
        print(random_list)
        
        print("Lists a and b are: ")
        if is_alias(random_list, alias): 
            print("aliases")
        else: 
            print("NOT aliases")
        
        a = list("equivalence")
        b = a[:]
        print("List a = ", a)
        print("List b = ", b)
        print("Lists a and b are equal? ", a == b)
        print("Lists a and b are: ")
        if is_alias(a, b): 
            print("aliases")
        else: 
            print("NOT aliases")
        print()
        print("String Objects")
        word1 = 'Wow'
        word2 = 'Wow'
        print('word1 =', word1)
        print('word2 =', word2)
        print('Equality: ', word1 == word2, '\nAlias: ', word1 is word2)
        print("Objects")
        obj1 = None
        obj2 = None
        print('Equality: ', obj1 == obj2, '\nAlias: ', obj1 is obj2)
    except Exception as e:
        print(e)
        

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()

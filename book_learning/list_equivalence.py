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
        is_alias = lambda x,y: x is y
        input_size = int(input("Enter list size: "))
        random_list = create_random_list(input_size)
        print(random_list)
        alias = random_list
        alias[0] = 55
        print(random_list)
        
        print("Lists a and b are: ", end = ' ')
        if is_alias(random_list, alias): 
            print("aliases")
        else: 
            print("NOT aliases")
        
        a = list("equivalence")
        b = a[:]
        print("List a = ", a)
        print("List b = ", b)
        print("Lists a and b are equal? ", a == b)
        print("Lists a and b are: ", end = ' ')
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
    except():
        print("Error: ")
        

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
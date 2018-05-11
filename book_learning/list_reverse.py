#!/usr/bin/python -tt
# Source:
# LEARNING TO PROGRAM WITH PYTHON
# Richard L. Halterman
"""
Different ways of reversing a list
"""

def reverse_halterman(lst):
    '''
    Recursive approach
    '''
    return [] if len(lst) == 0 else reverse_halterman(lst[1:]) + lst[0:1]


# Define a main() 
def main():
    name = 'Halterman'
    print(reverse_halterman(list(name)))
    
    # Standard Library:
    # iterator
    for item in reversed(list(name)):
        print(item, end = ' ')
    print()
    #list method()
    listreversed = list(name)
    listreversed.reverse() # returns None like list().sort()
    print(listreversed)
    
    
    

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()

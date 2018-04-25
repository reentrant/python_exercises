#!/usr/bin/python -tt
# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/
'''
Practice Python Sorting with python 3
Created on 24/04/2018

@author: jruiz
'''
    ## Write a little function that takes a string, and returns its last letter.
    ## This will be the key function (takes in 1 value, returns 1 value).
def MyFn(s):
    return s[-1]

'''
the sorted(list) function, which takes a list and returns a new list with those
elements in sorted order. The original list is not changed.
Custom Sorting With key=
'''
def custom_sorting():
    a = [5, 1, 4, 3]
    print("sort method vs sorted built-in function")
    print("Original: ", a)
    new_list = sorted(a)
    print("sorted() built-in function: ", new_list)
    print("Original: ", a)
    b = a.sort() ## NO incorrect, sort() returns None
    print("list.sort() method returns: ", b)
    print("Original: ", a)
    
    print("Using the sorted() function with optional argument :")
    print(sorted(a, reverse = True))
    print()
    
    # Other example:
    print("# Other example:")
    strs = ['aa', 'BB', 'zz', 'CC']
    print(sorted(strs))  ## ['BB', 'CC', 'aa', 'zz'] (case sensitive)
    print(sorted(strs, reverse = True))   ## ['zz', 'aa', 'CC', 'BB']
    print()
    
    #===========================================================================
    #Custom Sorting With key=
    #===========================================================================
    print("Custom Sorting With key = obj.len")
    strs = ['ccc', 'aaaa', 'd', 'bb']
    print (sorted(strs, key=len))  ## ['d', 'bb', 'ccc', 'aaaa']
    print()
    print("# Other example:")
    print("Custom Sorting With key = str.lower")
    ## "key" argument specifying str.lower function to use for sorting
    print (sorted(strs, key=str.lower))  ## ['aa', 'BB', 'CC', 'zz']
    print()
    print("# Other example:")
    print("Custom Sorting With key = myFunction")
    ## Say we have a list of strings we want to sort by the last letter of the string.
    strs = ['xc', 'zb', 'yd' ,'wa']
    ## Now pass key=MyFn to sorted() to sort by the last letter:
    print (sorted(strs, key=MyFn))  ## ['wa', 'zb', 'xc', 'yd']
    print()
    
def tuples():
    tuple = (1, 2, 'hi')
    print(len(tuple))  ## 3
    print(tuple[2])    ## hi
    tuple[2] = 'bye'  ## NO, tuples cannot be changed
    tuple = (1, 2, 'bye')  ## this works
    print()

'''
A list comprehension is a compact way to write an expression that expands to
a whole list.
The syntax is [ expr for var in list ] -- the for var in list looks like a 
regular for-loop, but without the colon (:). The expr to its left is evaluated 
once for each var element to give the values for the new list.
'''
def list_comprehensions():
    print("List Comprehensions")
    print("Example 1: squares:")
    #===========================================================================
    # here is the list comprehension to compute a list of their squares 
    #===========================================================================
    nums = [1, 2, 3, 4]
    squares = [ n * n for n in nums ]   ## [1, 4, 9, 16]
    print(squares)
    print()
    print("Example 2: shouting: ")
    #===========================================================================
    # Example: here each string is changed to upper case with '!!!' appended:
    #===========================================================================
    strs = ['hello', 'and', 'goodbye']
    shouting = [ s.upper() + '!!!' for s in strs ]
    print(shouting)## ['HELLO!!!', 'AND!!!', 'GOODBYE!!!']
    print()
    print("Example 3: filtering with if: ")
    #===========================================================================
    # You can add an if test to the right of the for-loop to narrow the result. 
    # The if test is evaluated for each element, including only the elements 
    # where the test is true.
    #===========================================================================
      ## Select values <= 2
    nums = [2, 8, 1, 6]
    small = [ n for n in nums if n <= 2 ]  ## [2, 1]
    print(small)
    print()
    print("Example 4: filtering with if: ")
    ## Select fruits containing 'a', change to upper case
    fruits = ['apple', 'cherry', 'bannana', 'lemon']
    afruits = [ s.upper() for s in fruits if 'a' in s ]
    print(afruits)
    ## ['APPLE', 'BANNANA']

if __name__ == '__main__':
    custom_sorting()
#     tuples()
    list_comprehensions()
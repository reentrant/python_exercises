'''
Created on 09/01/2018

@author: jruiz

    factorial(0) = 1                    Base Case
    factorial(n) = n*factorial(n-1)    Recursive Case
# Define a procedure, factorial, that takes a natural number as its input, and
# returns the number of ways to arrange the input number of items.
'''

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    


if __name__ == '__main__':
    print (factorial(0))
#>>> 1

    print (factorial(5))
    #>>> 120
    
    print (factorial(10))
#>>> 3628800
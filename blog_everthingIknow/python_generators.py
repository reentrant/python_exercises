#!/usr/bin/python -tt
# Improve Your Python: 'yield' and Generators Explained
# https://jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/
'''
Practice generators with python 3
Created on 24/04/2018
@author: jruiz
'''

import random
from math import factorial

'''
Wilson's theorem: http://en.wikipedia.org/wiki/Wilson's_theorem
In number theory, Wilson's theorem states that a natural number n > 1 is a
a prime number if and only if
    (n-1) = (n-1)! mod n.
'''
def is_prime(n):
    return n-1 == factorial(n-1) % n

def get_primes_wListComprehensions(input_list):
    return [n for n in input_list if is_prime(n)]

'''
Based on a finite list as input identify the prime numbers
'''
def fun_with_a_finite_list():
    finite_list = []
    for _ in range(10):
        finite_list.append(random.randint(1, 100))
    print(finite_list)
    print(sorted(get_primes_wListComprehensions(finite_list)))
    
'''
    What if get_primes could simply return the next value instead of 
    all the values at once? 
    It wouldn't need to create a list at all.
    No list, no memory issues!!!
'''
def get_primes_generator_function(n):# starting point
#     MAXIMUM_RECURSION_DEPTH_EXCEEDED = 997
    while n < 50:
        if is_prime(n):
            yield n
        n += 1
    return
    
'''
Based on an infinite list [from start to infinity]
identify the prime numbers
    # my_generator = simple_generator()
    # print(next(my_generator))
'''
def fun_with_an_infinite_list():
    start = 3
    i = 0
    #===========================================================================
    # a generator is a type of iterator and it can be used in a for loop:
    #===========================================================================
    for prime in get_primes_generator_function(start):
        print (prime, sep = ' ', end = ' ')
        i += 1
        if i % 10 == 0:
            print()
    
    
    
if __name__ == '__main__':
    fun_with_a_finite_list()
    fun_with_an_infinite_list()
    once_more = get_primes_generator_function(5) # new generator
    print(next(once_more))
    
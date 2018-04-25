#!/usr/bin/python -tt
# Improve Your Python: 'yield' and Generators Explained
# https://jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/
'''
Practice with python 3
Created on 24/04/2018
@author: jruiz
'''
import math
import random

'''
Wilson's theorem: http://en.wikipedia.org/wiki/Wilson's_theorem
In number theory, Wilson's theorem states that a natural number n > 1 is a
a prime number if and only if
    (n-1) = (n-1)! mod n.
'''
def find_a_prime(n):
    return factorial(n-1) % n

def factorial(n):
    if n>1:
        return n*(factorial(n-1))
    else:
        return 1

def get_primes(input_list):
    return [n for n in input_list if n-1 == find_a_prime(n)]


def fun_with_prime_numbers():
    my_list = []
    for i in range(10):
        my_list.append(random.randint(1, 100))
    print(my_list)
    print(get_primes(my_list))
    

if __name__ == '__main__':
    fun_with_prime_numbers()
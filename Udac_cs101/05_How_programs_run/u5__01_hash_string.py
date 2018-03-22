# -*- coding: utf-8 -*-
'''
Created on 8/01/2018
@author: jruiz
'''

def bad_hash_string(keyword, buckets):
    return ord(keyword[0]) % buckets

# Define a function, hash_string,
# that takes as inputs a keyword
# (string) and a number of buckets,
# and returns a number representing
# the bucket for that keyword.

def hash_string(keyword,buckets):
    weight = 0
    for c in keyword:
        weight = (weight + ord(c)) % buckets
    return weight



print hash_string('a',12)
#>>> 1

#print hash_string('b',12)
#>>> 2

print hash_string('a',13)
#>>> 6

#print hash_string('au',12)
#>>> 10

print hash_string('udacity',12)
#>>> 11

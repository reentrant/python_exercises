# -*- coding: utf-8 -*-

def bad_hash_string(keyword, buckets):
    return ord(keyword[0]) % buckets

def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()

    except:
        return "error"
# Define a function, hash_string,
# that takes as inputs a keyword
# (string) and a number of buckets,
# and returns a number representing
# the bucket for that keyword.
DEBUG = False
def hash_string(keyword,buckets):
    weight = 0
    for c in keyword:
        weight = (weight + ord(c)) % buckets
    return weight

def test_hash_function(func, keys, size):
    results = [0] * size
    keys_used = []
    for w in keys:
        hashvalue = func(w,size)
        results[hashvalue] += 1
        keys_used.append(w)
    return results



#print hash_string('a',12)
##>>> 1

#print hash_string('b',12)
##>>> 2

#print hash_string('a',13)
##>>> 6

#print hash_string('au',12)
##>>> 10

#print hash_string('udacity',12)
##>>> 11
#===============================================================================
# Adventures of Sherlock Holmes
#===============================================================================
words = get_page('http://www.gutenberg.org/cache/epub/1661/pg1661.txt').split()
#print words
print test_hash_function(bad_hash_string, words, 12)
print

print test_hash_function(hash_string, words, 12)


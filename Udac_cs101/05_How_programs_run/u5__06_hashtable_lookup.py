# -*- coding: utf-8 -*-

# Define a procedure,

# hashtable_lookup(htable,key)

# that takes two inputs, a hashtable
# and a key (string),
# and returns the value associated
# with that key.

DEBUG = True

def hashtable_lookup(htable,key):
    bucket = hashtable_get_bucket(htable,key)
    if DEBUG:
        print bucket
    for e in bucket:
        if key in e:
            print e
            return e[1]
    return None  


def hashtable_add(htable,key,value):
    bucket = hashtable_get_bucket(htable,key)
    bucket.append([key,value])


def hashtable_get_bucket(htable,keyword):
    return htable[hash_string(keyword,len(htable))]

def hash_string(keyword,buckets):
    which_bucket = 0
    for s in keyword:
        which_bucket = (which_bucket + ord(s)) % buckets
    return which_bucket

def make_hashtable(nbuckets):
    table = []
    for unused in range(0,nbuckets):
        table.append([])
    return table


table = [[['Ellis', 11], ['Francis', 13]], [], [['Bill', 17], ['Zoe', 14]],
    [['Coach', 4]], [['Louis', 29], ['Nick', 2], ['Rochelle', 4]]]

print hashtable_lookup(table, 'Francis')
#>>> 13

print hashtable_lookup(table, 'Louis')
#>>> 29

print hashtable_lookup(table, 'Zoe')
#>>> 14

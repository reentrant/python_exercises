#!/usr/bin/python -tt
# Source:
# LEARNING TO PROGRAM WITH PYTHON
# Richard L. Halterman
"""
Example: List Permutations
"""

from itertools import permutations
DEBUG = False
counter = 0

def permute(prefix, suffix):
    '''
    Recursively shifts all the elements in suffix into prefix
    '''
    global counter
    counter += 1
    if DEBUG:
        print("\tpermute args: ", "-" * 10, end = ' ')
        print(counter, prefix, suffix)
    suffix_size = len(suffix)
    if suffix_size == 0:
        print (prefix)
    else:
        for i in range(0, suffix_size):
            new_pref = prefix + [suffix[i]]
            if DEBUG:
                print(i," new_pre: -->", prefix, " ", [suffix[i]])
            # print(new_pref, end = ' ')
            new_suff = suffix[:i] + suffix[i + 1:]
            if DEBUG:
                print(i, "new_suff: -->", suffix[:i], suffix[i + 1:])
            # print(new_suff)
            permute(new_pref, new_suff)

def tab(n):
    print('\t' * n, end='')
        
def trace_permute(prefix, suffix, depth):
    suffix_size = len(suffix)
    if suffix_size == 0:
        pass
    else:
        for i in range(0, suffix_size):
            new_pre = prefix + [suffix[i]]
            new_suff = suffix[:i] + suffix[i + 1:]
            tab(depth)
            print(new_pre, new_suff, sep = ':')
            trace_permute(new_pre, new_suff, depth + 1)
    
    
def print_permutations(lst):
    '''
    Calls the recursive permute function
    '''
    permute([], lst)

# Define a main() function 
def main():
    print_permutations(list('abc'))
    print("=" * 20)
    trace_permute([], list("abc"), 0)
    print("=" * 20)
    name = 'iter'
    for p in permutations(list(name)):
        print(p)
    print("=" * 20)

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()

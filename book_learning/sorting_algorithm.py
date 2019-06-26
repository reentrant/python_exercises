#!/usr/bin/python -tt
# Source:
# LEARNING TO PROGRAM WITH PYTHON
# Richard L. Halterman

"""
Example: Fun With Prime Numbers
"""

import sys
import random
import time
'''
Creates a List of natural numbers
'''
def create_random_list(n):
    random_list = []
    for _ in range(n):
        element = random.randrange(1, 100)
#         random_list.append(element)  # Allow repetition
        if element not in random_list:
            random_list.append(element)
    return random_list
'''
Order the list lst by implementing the bubble sort or selection sort algorithm
'''        
def selection_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        small_ix = i 
        # find the smallest index to the right
        for j in range(i + 1, n):
            if lst[j] < lst[small_ix]:
                small_ix = j
        if i != small_ix:
            lst[i], lst[small_ix] = lst[small_ix], lst[i]
    print(lst)
    return # lst is a reference... so it is no need to return it...

'''
Linear Search Algorithm
'''
def linear_search(value, lst):
    index = None
    for i in range(len(lst)):
        if lst[i] == value:
            index = i
    assert(index == lst.index(value))
    return index

'''
Binary Search Algorithm
'''
def binary_search(value, sorted_lst):
    found_ix = None
    if value in sorted_lst:
        first_ix = 0
        last_ix = len(sorted_lst) - 1
        while first_ix <= last_ix:
            mid_ix = first_ix + (last_ix - first_ix) // 2
            if sorted_lst[mid_ix] == value:
                found_ix = mid_ix
                break
            elif value > sorted_lst[mid_ix]:
                first_ix = mid_ix + 1
            else:
                last_ix = mid_ix - 1
        assert(found_ix == sorted_lst.index(value))
        return found_ix
    else:
        return found_ix

'''
boolean function to check if a natural number is prime
'''
def is_prime(n):#n is a natural number
    prime_flag = True
    if n == 0 or n == 1:
        prime_flag = False
    else:
        counter = 0
        for i in range(1, n + 1):
            if n % i == 0:
                counter += 1
            else:
                # print("%d / %d remainder = %d " % (n, i, n % i))
                pass
            if counter > 2:
                prime_flag = False
                break
    return prime_flag

def get_primes(input_list):
    result_list = list()
    for element in input_list:
        if is_prime(element):
            result_list += [element]
    return result_list


# Define a main() function
def main():
    if len(sys.argv) >= 2:
        for e in  sys.argv:
            print(e)
        quit()
    else:
        size = random.randint(5, 1000)
        print(size)
        input_set = create_random_list(size)
    #===========================================================================
    # Selection Sort Algorithm
    #===========================================================================
    print("List (set) size = ", len(input_set))
#     print("Original list: ", input_set)
    working_set = input_set[:]
    start = time.process_time()
    selection_sort(input_set)
    print("Selection Sort elapsed = ", time.process_time() - start)
    start = time.process_time()
    sorted(working_set)
    print("Standard Library sorted() elapsed = ", time.process_time() - start)
    # print(input_set)
    print("=" * 20)
    #===========================================================================
    # Search Algorithms: Lets lookup the elements of prime_list in the input_set
    #===========================================================================
    primes_list = get_primes(input_set)
    print(primes_list)
    start = time.process_time()
    for e in primes_list:
#         index = 
        linear_search(e, input_set)
        # if index != None:
            # print("index = ", index)
    print("Linear Search t = ", time.process_time() - start)
    print("=" * 20)
    start = time.process_time()
    for e in primes_list:
#         index = 
        binary_search(e, input_set)
        # if index != None:
            # print("index = ", index)
    print("Binary Search t = ", time.process_time() - start)
    print("=" * 20)


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()

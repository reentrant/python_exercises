'''
Created on 28/02/2018

@author: jruiz

You have a list of integers, and for each index you want to find the product of
 every integer except the integer at that index.

Write a function get_products_of_all_ints_except_at_index() that takes a list 
of integers and returns a list of the products.

For example, given:

  [1, 7, 3, 4]

your function would return:

  [84, 12, 28, 21]

by calculating:

  [7 * 3 * 4,  1 * 3 * 4,  1 * 7 * 4,  1 * 7 * 3]

Do not use division in your solution.
'''
from functools import reduce

def get_products_of_all_ints_except_at_index(int_list):
    products = []
    i = 0
    while i < len(int_list):
        #=======================================================================
        # print int_list[before] 
        #=======================================================================
#         print (int_list[:i ], end = ' ')
        #=======================================================================
        # + int_list[after] 
        #=======================================================================
#         print (int_list[i + 1: ], end = ' ')
        #=======================================================================
        # elements before  + after
        #=======================================================================
        products.append(reduce(lambda x, y: x * y,
                                int_list[:i ] + int_list[i + 1: ]))
        i += 1
        print
    print
    return products


example = [1, 7, 3, 4, 0]
print (get_products_of_all_ints_except_at_index(example))

input_list = [3, 1, 2, 5, 6, 4]
print (get_products_of_all_ints_except_at_index(input_list))

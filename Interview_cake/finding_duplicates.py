'''
Created on 14/06/2018

@author: jruiz

Given 2 different lists of integers, 
write a function that will return their intersection.

Example:

[1,2,2,3] and [2,2,3,4] should intersect as [2,2,3] and not just [2,3].
'''
def find_duplicates(a, b):
    items = {}
    result = []
    for e in a:
        if e in items:
            items[e] += 1
        else:
            items[e] = 1
    for e in b:
        if e in items and items[e] > 0:
            result.append(e)
            items[e] -= 1
            
    return result


if __name__ == '__main__':
    lst_1 = [1, 2, 2, 3]
    lst_2 = [2, 2, 3, 4]
    print(find_duplicates(lst_1, lst_2)) 
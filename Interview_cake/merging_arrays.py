'''
Created on 09/05/2018

@author: jruiz

Data Structures and Loops: Sets

'''


def remove_duplicates_from_list(lst):
    new_lst = []
    for e in lst:
        if e in new_lst:
            continue
        else:
            new_lst.append(e)
    return new_lst


def build_a_set(limit):
    return set([x * x for x in range(1, limit) if x * x < limit])


def merge_two_lists(names1, names2):
    union_a_b = []
    for element in names1:
        if element not in union_a_b:
            union_a_b.append(element)
    for element in names2:
        if element not in union_a_b:
            union_a_b.append(element)
    return union_a_b


if __name__ == '__main__':
    lst = [1, 1, 2, 2, 3, 3]
    print("Original list: ", lst)
    print(remove_duplicates_from_list(lst))
    print('builtin set: ')
    print(set(lst))
    # Populate squares with the set of all integers less than 2000 that are
    # square numbers.
    squares = build_a_set(2000)
    print(squares)
    print(merge_two_lists(lst, [2, 3, 5]))



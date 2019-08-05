#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
from timer import timer


def get_list_with_next_minor_element(list_a, list_b):
    i = 0
    if list_a and list_b and list_a[i] < list_b[i]:
        alias = list_a
    elif not list_b:
        alias = list_a
    else:
        alias = list_b
    return alias


@timer(enable=True, display=True)
def merge_sorted_lists(list_a, list_b):
    """
    exercise from https://www.interviewcake.com
    In order to win the prize for most cookies sold, my friend Alice and I are going to merge our
    Girl Scout Cookies orders and enter as one unit.
    Each order is represented by an "order id" (an integer).
    We have our lists of orders sorted numerically already, in lists.
    Write a function to merge our lists of orders into one sorted list.
    """
    a_union_b = []
    while list_a or list_b:
        list_with_minor_element = get_list_with_next_minor_element(list_a, list_b)
        if list_with_minor_element[0] not in a_union_b:
            a_union_b.append(list_with_minor_element[0])
        list_with_minor_element.pop(0)
    return a_union_b


@timer(enable=True, display=True)
def use_builtins(list_a, list_b):
    return sorted(list_a + list_b)


my_list = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]
# # Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
# print(merge_sorted_lists(my_list, alices_list))
print(merge_sorted_lists(my_list, alices_list))
my_list = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]
print(use_builtins(my_list, alices_list))

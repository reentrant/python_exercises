'''
Created on 08/04/2019
'''
#!/bin/python

import math
import os
import random
import re
import sys


def traverse_sprint(sprint):
    pass


def test_maximum(results, maximum, dictionary, key):
    if dictionary[key] > maximum:
        results = [key]
        maximum = dictionary[key]
    elif dictionary[key] == maximum:
        results.append(key)
    return maximum, results


def getMostVisited(n, sprints):
    # The function is expected to return an INTEGER.
    # The function accepts following parameters:
    #  1. INTEGER n
    #  2. INTEGER_ARRAY sprints
    # Write your code here
    start = end = 0
    markers = {}
    results = []
    maximum = 0
    for i in range(len(sprints)-1):
        sprint = sprints[i: i+2]
        #===========================================================================================
        # traverse sprints
        #===========================================================================================
        if sprint[0] < sprint[1]:
            start = sprint[0]
            end = 1 + sprint[1]
        else:
            start = sprint[1]
            end = sprint[0] + 1
        for j in range(start, end):
            if j in markers:
                markers[j] += 1
            else:
                markers[j] = 1
            if not markers[j] < maximum:
                maximum, results = test_maximum(results, maximum, markers, j)
        print(results)
    #===========================================================================================
    # Maximum
    #===========================================================================================
#     sorted_visits = sorted(markers.items(), key = lambda x: x[1], reverse = True )
#     maximum = sorted_visits[0][1]
#     print maximum
    return min(results)

    #===========================================================================================
    # How many
    #===========================================================================================
#     result = [maximum]
#     for m in range(1, len(sorted_visits)):
#         if sorted_visits[m][1] < maximum:
#             break
#         else:
#             result.append(sorted_visits[m][0])
#     return min(result)


if __name__ == '__main__':
    number = 9
    # 4
    test_sprints = [9, 7, 3, 1]
    result = getMostVisited(number, test_sprints)
    print(result)

# -*- coding: utf-8 -*-
'''
Created on 09/01/2018

@author: jruiz

# Define a procedure is_palindrome, that takes as input a string, and returns a
# Boolean indicating if the input string is a palindrome.

# Base Case: '' => True
# Recursive Case: if first and last characters don't match => False
# if they do match, is the middle a palindrome?
'''
import time


def time_execution(code):
    start = time.perf_counter()
    result = eval(code)
    run_time = time.perf_counter() - start
    return result, run_time


def recursive_check_palindrome(s):
    if s == '':
        return True
    elif len(s) == 1:
        return True
    elif len(s) > 1:
        if s[0] == s[-1]:
            return recursive_check_palindrome(s[1:-1])
        else:
            return False


def iterative_check_palindrome(s):
    for i in range(0, len(s) // 2):
        if s[i] != s[-(i + 1)]:
            return False
    return True


if __name__ == '__main__':
    print(recursive_check_palindrome(''))
    #>>> True
    print(recursive_check_palindrome('level'))
    #>>> False
    print(recursive_check_palindrome('abba'))
    #>>> True
    print(time_execution('recursive_check_palindrome(\'amanaplanacanalpanama\')'))
    print(time_execution('iterative_check_palindrome(\'amanaplanacanalpanama\')'))
    #Are we not pure? �No, sir!� Panama�s moody Noriega brags. �It is garbage!� Irony dooms a man�a prisoner up to new era.
    print(time_execution('recursive_check_palindrome(\'ArewenotpureNosirPanamasmoodyNoriegabragsItisgarbageIronydoomsamanaprisoneruptonewera\')'))
    print(time_execution('iterative_check_palindrome(\'ArewenotpureNosirPanamasmoodyNoriegabragsItisgarbageIronydoomsamanaprisoneruptonewera\')'))

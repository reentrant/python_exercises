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
    start = time.clock()
    result = eval(code)
    run_time = time.clock() - start
    return result, run_time

def is_palindrome(s):
#     print s
    if s == '':
        return True
    elif len(s) == 1:
        return True
    elif len(s) > 1:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False
    
def iterative_palindrome(s):
    for i in range(0, len(s) // 2):
        if s[i] != s[-(i + 1)]:
            return False
    return True
    
print(is_palindrome(''))
#>>> True
print(is_palindrome('level'))
#>>> False
print(is_palindrome('abba'))
#>>> True
print(time_execution('is_palindrome(\'amanaplanacanalpanama\')'))
print(time_execution('iterative_palindrome(\'amanaplanacanalpanama\')'))
#Are we not pure? �No, sir!� Panama�s moody Noriega brags. �It is garbage!� Irony dooms a man�a prisoner up to new era.
print(time_execution('is_palindrome(\'ArewenotpureNosirPanamasmoodyNoriegabragsItisgarbageIronydoomsamanaprisoneruptonewera\')'))
print(time_execution('iterative_palindrome(\'ArewenotpureNosirPanamasmoodyNoriegabragsItisgarbageIronydoomsamanaprisoneruptonewera\')'))

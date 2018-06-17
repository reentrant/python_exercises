#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
'''
Created on 01/06/2018
In this challenge, the user enters a string and a substring. You have to print the 
number of times that the substring occurs in the given string. 
String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.

Input Format

The first line of input contains the original string. 
The next line contains the substring.

Constraints

 
Each character in the string is an ascii character.

Output Format

Output the integer number indicating the total number of occurrences of the substring 
in the original string.

Sample Input

ABCDCDC
CDC
Sample Output

2

@author: jruiz
'''
import time

class Stopwatch:
    def __init__(self):
        self.start = time.clock()
        
    def stop(self):
        self.now = time.clock()
        self.elapsed_time = self.now - self.start
        return self.elapsed_time
    
    def reset(self):
        self.start = time.clock()


def count_substring_enhanced(string, sub_string):
    times = 0
    ix = 0
    while string.find(sub_string, ix) > -1:
        ix = string.find(sub_string, ix)
        ix += 1
        times += 1
    return times

def count_substring(string, sub_string):
    times = 0
    i = 0
    index = i
    while i < len(string):
        index = string.find(sub_string, index)
        if index >= 0:
            index += 1
            i = index
            times += 1
        else:
            break
    return times

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    stpwtch = Stopwatch()
    count = count_substring(string, sub_string)
    print(count)
    print(stpwtch.stop())
    stpwtch.reset()
    count = count_substring_enhanced(string, sub_string)
    print(count)
    print(stpwtch.stop())
    
'''
Created on 01/06/2018

@author: jruiz
Python has built-in string validation methods for basic data. It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.


Task

You are given a string . 
Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

Input Format

A single line containing a string .

Constraints


Output Format

In the first line, print True if  has any alphanumeric characters. Otherwise, print False. 
In the second line, print True if  has any alphabetical characters. Otherwise, print False. 
In the third line, print True if  has any digits. Otherwise, print False. 
In the fourth line, print True if  has any lowercase characters. Otherwise, print False. 
In the fifth line, print True if  has any uppercase characters. Otherwise, print False.

Sample Input

qA2
Sample Output

True
True
True
True
True

'''
from functools import reduce
# line = input().split()
# s = list(map(int, line))
s = input()

result = reduce(lambda x,y: x or y, [c.isalnum() for c in s] )
print(result)
result = reduce(lambda x,y: x or y, [c.isalpha() for c in s] )
print(result)
result = reduce(lambda x,y: x or y, [c.isdigit() for c in s] )
print(result)
result = reduce(lambda x,y: x or y, [c.islower() for c in s] )
print(result)
result = reduce(lambda x,y: x or y, [c.isupper() for c in s] )
print(result)

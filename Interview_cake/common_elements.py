'''
Created on 21/08/2016

@author: jruiz
'''
# Write a function that accepts two arbitrary strings and 
# returns a new string containing the unique common characters from both inputs. 
#An O(n) solution is preferred.
# 
# Write sufficient unit test cases to exercise the complexity and logical boundaries of
# your function.
# 
# 
# Input:
# The function must accept two string parameters.
# 
# 
# Output:
# The function must return a string.


def common_chars(a, b):
    a = set(a.lower())
    b = set(b.lower())
    unique = a.intersection(b)
    return "".join(unique)
    
print(common_chars('Julian', 'Avril'))
print(common_chars('Marisa', 'Avril'))
print(common_chars('World', ''))
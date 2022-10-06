'''
Created on 22/01/2018

@author: jruiz
'''
#===============================================================================
# Lambda Operator
#===============================================================================
print("lambdas")
f = lambda x, y: x + y
print (f(1,1))
#===============================================================================
# the map() function
#===============================================================================
print("maps")


def fahrenheit(t):
    return (9/5.0 * t + 32)


temp_list_C = [0, 32, 37, 38]

    
F = map(fahrenheit, temp_list_C)
print (list(F))

Fahrenheit = map(lambda t: 9/5.0 * t + 32, temp_list_C)
print (list(Fahrenheit))

#===============================================================================
# Filtering
#===============================================================================
def fibonacci(n):
    assert n >= 0
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n -2)
    
def f_list(x):
    return map(lambda x: fibonacci(x), range(x))

simple_generator = f_list(10)
print("fibonacci(10)")
print (list(f_list(10)))

print("filters")
result = filter(lambda x: x % 2, simple_generator)
print("type of (filter(lambda x: x % 2, simple_generator)){}".format(type(result)))
print(result)

print("#======================================================================")
# print("Change in python3")
# print("#======================================================================")
# result = filter(lambda x: x % 2 == 0, simple_generator)# it works in python 2.7
# print(list(result), end = '')
# print("\t# However it worked in python 2.7")

result = filter(lambda x: x % 2 == 0, f_list(10))
print(type(result))
print(result)

#===============================================================================
# Reducing a List
# example: Calculating the sum of the numbers from 1 to 100:
#===============================================================================
from functools import reduce
print("reduce")
suma = reduce(lambda x, y: x + y, range(1, 101))
print(suma)


#===============================================================================
# Find the Max Value in a List
#===============================================================================
maximum = reduce(lambda a, b: a if (a > b) else b, [47, 11, 42, 102, 13])
print(maximum)

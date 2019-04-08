'''
Created on 09/01/2018

@author: jruiz
# Define a procedure, fibonacci, that takes a natural number as its input, and
# returns the value of that fibonacci number.

# Two Base Cases:
#    fibonacci(0) => 0
#    fibonacci(1) => 1

# Recursive Case:
#    n > 1 : fibonacci(n) => fibonacci(n-1) + fibonacci(n-2)
'''


def fibonacci(n):
    current = 0
    after = 1
    for _ in range(0, n):
        temp = current + after
        current = after
        after = temp
    return current

print(fibonacci(0))
#>>> 0
print(fibonacci(1))
#>>> 1
print(fibonacci(2))
print(fibonacci(3))

print(fibonacci(15))
print(fibonacci(36))

def f_list(x):
    return list(map(fibonacci, range(x)))

print(f_list(11))

fib = f_list(11)

result = list(filter(lambda x: x % 2, fib))
print(result)

result = list(filter(lambda x: x % 2 == 0, fib))
print(result)

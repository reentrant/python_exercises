'''
Created on Aug 11, 2018

@author: Julian

Test input:
3
1000000007
100000003
1000003
'''
import math


def prime(value):
    if value == 2:
        return True
    if value < 2:
        return False
    if value % 2 == 0:
        return False
    stop = math.sqrt(value)
    i = 3
    while i <= stop:
        if value % i == 0:
            return False
        i += 2
    return True


N = int(input())
for _ in range(N):
    print("Prime") if prime(int(input())) else print("Not prime")

# from math import factorial, sqrt
# 
# class Primer(object):
#         
#     def __init__(self):
#         self.MAXIMUM_RECURSION_DEPTH_EXCEEDED = 997
# 
#     def get_primes_generator_function(self, n, stop):# starting point
#         while n < stop:
#             if Primer.is_prime(self, n):
#                 yield n                
#             if n % 2 == 0:   
#                 n += 1
#             else:
#                 n += 2
#         return
#   
#     def is_prime(self, n):        
#         if n == 0 or n == 1:
#             return False
#         elif n <= self.MAXIMUM_RECURSION_DEPTH_EXCEEDED:
#             return n - 1 == factorial(n - 1) % n
#         else:
#             start = 2
#             stop = int(sqrt(n)) + 1
#             for is_prime in self.get_primes_generator_function(start, stop):
#                 if n % is_prime == 0:
#                     return False
#             return True
# 
# if __name__ == '__main__':
#     test_cases = int(input())
#     if 1 <= test_cases <= 30:
#         for _ in range(test_cases):
#             n = int(input())
#             if 1 <= n < 2 * 10 ** 9:
#                 test = Primer()
#                 if test.is_prime(n):
#                     print('Prime')
#                 else:
#                     print('Not is_prime')

'''
Created on Aug 11, 2018

@author: Julian

Test input:
3
1000000007
100000003
1000003
'''

from math import sqrt

class Primer(object):
        
    def __init__(self):
        self.MAXIMUM_RECURSION_DEPTH_EXCEEDED = 997

    def is_prime(self, n):
        prime_flag = True
        stop = int(sqrt(n))
        if n == 0 or n == 1:
            prime_flag = False
        else:
            start = 2
            for i in range(start, stop + 1):
                if n % i == 0:
                    prime_flag = 0
                    break
        return prime_flag


if __name__ == '__main__':
    test_cases = int(input())
    if 1 <= test_cases <= 30:
        for _ in range(test_cases):
            n = int(input())
            if 1 <= n < 2 * 10 ** 9:
                test = Primer()
                if test.is_prime(n):
                    print('Prime')
                else:
                    print('Not prime')

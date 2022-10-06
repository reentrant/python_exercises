'''
Created on 22/01/2018

@author: jruiz
'''


def squares():
    return [n * n for n in range(10)]


def squares_narrow():
    return [n * n for n in range(10) if n < 5]


def mult_tables(n):
    return [n * i for i in range(10)]


def mult_tables_narrow(n):
    return [n * i for i in range(10) if i < 4]


strings = ['hello', 'and', 'goodbye']


def shouting():
    return [s.upper() + '!!!' for s in strings]


def shouting_narrow():
    return [s.upper() + '!!!' for s in strings if 'a' in s]


def pitagoras():
    return [(x, y, z) for x in range(1, 30)\
            for y in range(x, 30)\
            for z in range(y, 30) if x * x + y * y == z * z]


colours = ["red", "green", "yellow", "blue"]
things = ["house", "car"]


def cross_product():
    return [(x, y) for x in colours for y in things]

if __name__ == '__main__':
    print(squares_narrow())
    print(mult_tables_narrow(2))
    print(shouting_narrow())
    print(pitagoras())
    print(cross_product())
    print("=" * 80)
    #===========================================================================
    # Generators
    #===========================================================================
    print("Generators")
    squares = (n * n for n in range(10))
    print(squares)
    print(list(squares))
    #===========================================================================
    # Prime Numbers Calulation using the sieve of Eratosthenes
    #===========================================================================
    noprimes = [j for i in range(2, 8) for j in range(i*2, 100, i)]
    primes = [x for x in range(2, 100) if x not in noprimes]
    print("=" * 80)
    #===========================================================================
    # Set Comprehension
    #===========================================================================
    from math import sqrt
    n = 100
    sqrt_n = int(sqrt(n))
    no_primes = {j for i in range(2,sqrt_n) for j in range(i*2, n, i)}
    primes = {i for i in range(n) if i not in no_primes}
    print (primes)

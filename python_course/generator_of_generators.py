"""
Created on 14/06/2018
# A generator of generators

@author: jruiz
"""


def fibonacci():
    """Ein Fibonacci-Zahlen-Generator"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def first_n(g, n):
    for _ in range(n):
        yield next(g())


if __name__ == '__main__':
    import sys
    print(sys.version)
    simple_generator = fibonacci()
    for e in range(5):
        print(next(simple_generator))
    print("===")
    first_n(simple_generator, 5)


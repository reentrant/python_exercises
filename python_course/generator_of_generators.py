'''
Created on 14/06/2018

@author: jruiz
'''
#===============================================================================
# A generator of generators
#===============================================================================
def fibonacci():
    """Ein Fibonacci-Zahlen-Generator"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def generator_of_generators(g, n):
    for _ in range(n):
#         print(g.next())
        yield g.next()

if __name__ == '__main__':
    #===========================================================================
    # A simple generator
    #===========================================================================
    simple_generator = fibonacci()
    for e in range(5):
        print(next(simple_generator))
        
    #===========================================================================
    # A generator of generators (it worked in python 2.7...)
    #===========================================================================
    generator_of_generators(fibonacci(), 10)

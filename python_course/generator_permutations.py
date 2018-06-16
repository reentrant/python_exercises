'''
Like functions generators can be recursively programmed. 
The following example 
is a generator to create all the permutations of a given list of items. 
@author: https://www.python-course.eu/generators.php
'''
def permutations(items):
    n = len(items)
    if n==0: yield []
    else:
        for i in range(len(items)):
            for cc in permutations(items[:i]+items[i+1:]):
                yield [items[i]]+cc

for p in permutations([1, 2]):
    print(p)

for p in permutations(['1','2','3']): 
    print(p)
# 
# for p in permutations( list("game")): 
#     print(p)
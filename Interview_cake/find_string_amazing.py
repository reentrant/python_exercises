'''
Created on 26/10/2016
Created on 16/06/2018

@author: jruiz

@summary: find the needle (word with chars given in any order == anagram) inside of the
 haystack
'''
import sys
import time
from itertools import permutations

class Stopwatch:
    def __init__(self):
        self.start = time.clock()
        
    def stop(self):
        self.now = time.clock()
        self.elapsed_time = self.now - self.start
        return self.elapsed_time
    
    def reset(self):
        self.start = time.clock()

DEBUG = False

haystack = "abdcgab"
needle = "ab"    
    
def getAnagramIndexes(haystack, needle):
    index_lst = []
    for e in permutations(list(needle)):
        i = 0
        anagram = "".join(e)
        if DEBUG:
            print(anagram)
        while haystack.find(anagram, i) > -1:
            ix = haystack.find(anagram, i)
            index_lst.append(ix)
            i = ix + 1
            if DEBUG:
                print(ix)
    return index_lst
        
stpwtch = Stopwatch()    
print(getAnagramIndexes(haystack, needle))
#[0, 5]
print(stpwtch.stop())
print(sys.executable)


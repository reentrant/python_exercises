#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys
import re
import time
# +++your code here+++
class Stopwatch:
    def __init__(self):
        self.start = time.clock()
        
    def stop(self):
        self.now = time.clock()
        self.elapsed_time = self.now - self.start
        return self.elapsed_time
    
    def reset(self):
        self.start = time.clock()
        
def count_words(filename):
    """Count how many times each unique word occurs in text."""
    with open(filename, "r") as f:
        text = f.read()
        
#     word_list = dict()  # dictionary of { <word>: <count> } pairs to return
    word_list = dict()
    t = Stopwatch()
    
    new_word = ''
    for c in text:
        if c in ' ,.;:!?*/-+_"()[]`' or c == '\r' or c== '\n':
            if new_word:
                if new_word in word_list.keys():
                    word_list[new_word] += 1
                else:
                    word_list[new_word] = 1
                new_word = ''
        else:
            new_word += c.lower()
    
    if new_word:
        if new_word in word_list.keys():
            word_list[new_word] += 1
        else:
            word_list[new_word] = 1
#     print(word_list)
    print(t.stop())
    return word_list

# Define print_words(filename) and print_top(filename) functions.
def print_words(filename):
    """
    counts how often each word appears in the text and prints:
    word1 count1
    word2 count2
    """
    counts = count_words(filename)
    for key in sorted(counts.keys()):
        print("{}\t\t{}".format(key, counts[key]))
        
def print_top(filename):
    """
    prints just the top 20 most common words sorted
    so the most common word is first, then the next most common, and so on.
    """
    counts = count_words(filename)
    
    sorted_counts = sorted(counts.items(), key = lambda pair: pair[1],
                            reverse = True )
    for k, v in sorted_counts[:20]:
        print("{}\t\t{}".format(k, v))
    
    
    
    
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
    if len(sys.argv) != 3:
        print ('usage: ./wordcount.py {--count | --topcount} file')
        print(sys.argv)
        sys.exit(1)
    
    option = sys.argv[1]
    filename = sys.argv[2]

    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print ('unknown option: ' + option)
        sys.exit(1)

if __name__ == '__main__':
    main()

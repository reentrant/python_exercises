'''
Created on 08/05/2018

@author: jruiz
'''
"""Splitting text data into tokens."""

import re

def sent_tokenize(text):
    """Split text into sentences."""
    # TODO: Split text by sentence delimiters (remove delimiters)
    # TODO: Remove leading and trailing spaces from each sentence
    
    # TODO: Return a list of sentences (remove blank strings)
    return re.findall('([A-Z][^.?!]+)[\.?!]', text)


def word_tokenize(sent):
    """Split a sentence into words."""
    
    # TODO: Split sent by word delimiters (remove delimiters)
    
    # TODO: Remove leading and trailing spaces from each word
    
    # TODO: Return a list of words (remove blank strings)
    return sent.split()


def test_run():
    """Called on Test Run."""

    text = "The first time you see The Second Renaissance it may look boring. Look at it at least twice and definitely watch part 2. It will change your view of the matrix. Are the human people the ones who started the war? Is AI a bad thing?"
    print("--- Sample text ---", text, sep="\n")
    
    sentences = sent_tokenize(text)
    print("\n--- Sentences ---")
    print(sentences)
    
    print("\n--- Words ---")
    for sent in sentences:
        print(sent)
        print(word_tokenize(sent))
        print()  # blank line for readability

if __name__ == "__main__":
    test_run()
from functools import reduce


def validate_strings():
    """
    Created on 01/06/2018

    Python has built-in string validation methods for basic data. It can check if a string
    is composed of alphabetical characters, alphanumeric characters, digits, etc.


    Task

    You are given a string .
    Your task is to find out if the string  contains: alphanumeric characters, alphabetical
     characters, digits, lowercase and uppercase characters.

    Input Format

    A single line containing a string .

    Constraints


    Output Format

    In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
    In the second line, print True if  has any alphabetical characters. Otherwise, print False.
    In the third line, print True if  has any digits. Otherwise, print False.
    In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
    In the fifth line, print True if  has any uppercase characters. Otherwise, print False.

    Sample Input

    qA2
    Sample Output

    True
    True
    True
    True
    True
    :return:
    """
    s = input()

    result = reduce(lambda x,y: x or y, map(str.isalnum, s))
    print(result)
    result = reduce(lambda x,y: x or y, [c.isalpha() for c in s])
    print(result)

    result = reduce(lambda x,y: x or y, map(str.isdigit, s))
    print(result)

    result = reduce(lambda x,y: x or y, map(str.islower, s) )
    print(result)
    result = reduce(lambda x,y: x or y, [c.isupper() for c in s])
    print(result)


def is_palindrome(word):
    """
    Checks if a given word is a palindrome. Character case should be ignored.
    :param word:
    :return: True when the given word reads the same backward and forward.
    """
    palindrome = True
    start = 0
    end = len(word) - 1
    if end == 0 or end == -1:
        palindrome = True
        return palindrome
    else:
        middle = len(word) // 2
        while start < middle:
            if word[start].lower() == word[end].lower():
                pass
            else:
                palindrome = False
                break
            start += 1
            end -= 1
    return palindrome


class Path:
    """
    Root path is '/'.
    Path separator is '/'.
    Parent directory is addressable as '..'.
    Directory names consist only of English alphabet letters (A-Z and a-z).
    The function should support both relative and absolute paths.
    The function will not be passed any invalid paths.
    Do not use built-in path-related functions.
    """
    def __init__(self, path):
        self.current_path = path
        self.tokens = path.split('/')

    def cd(self, new_path):
        if new_path.startswith("/"):
            pass
        else:
            print("It is relative")



if __name__ == '__main__':
    # print(is_palindrome('Deleveled'))
    # print(is_palindrome("Rats live on no evil star"))
    # print(is_palindrome(""))
    # print(is_palindrome("a"))
    # print(is_palindrome("rr"))
    # print(is_palindrome("aba"))
    path = Path('/a/b/c/d')
    path.cd('../x')
    print(path.tokens)
    print(path.current_path)


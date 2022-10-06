"""
A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both
 ends in the binary representation of N.
For example, number 9 has binary representation 1001 and contains a binary gap of length 2.
The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3.
The number 20 has binary representation 10100 and contains one binary gap of length 1.
The number 15 has binary representation 1111 and has no binary gaps.
The number 32 has binary representation 100000 and has no binary gaps.

Write a function:

def solution(N)

that, given a positive integer N, returns the length of its longest binary gap. The function should return 0
if N doesn't contain a binary gap.
For example, given N = 1041 the function should return 5, because N has binary representation 10000010001
and so its longest binary gap is of length 5.
Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647].
Copyright 2009–2022 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
"""
import math


def solution(n):
    # print(n, n.bit_length(), bin(n))
    # for i in range(n.bit_length()):
    #     print(n // 2)
    #     print(n % 2)
    #     print()
    #     n = n // 2

    if n == 2 ** n.bit_length() - 1:
        return 0
    elif n == 2 ** (n.bit_length() - 1):
        return 0

    max_gap = 0
    counter = 0
    for bit in bin(n).replace('0b1', ''):
        if bit == '0':
            counter += 1
        else:
            if counter > max_gap:
                max_gap = counter
            counter = 0
    return max_gap


if __name__ == "__main__":
    tests = [5, 6, 9]

    for number in tests:
        print(">>> ", solution(number))
    print("julian".strip())
    print("".join(list("julian")))

    print(max(2,5, 8))



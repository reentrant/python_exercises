'''

@author: jruiz
'''
# Define a procedure, total_enrollment,
# that takes as an input a list of elements,
# where each element is a list containing
# three elements: a university name,
# the total number of students enrolled,
# and the annual tuition fees.

# The procedure should return two numbers,
# not a string, 
# giving the total number of students
# enrolled at all of the universities
# in the list, and the total tuition fees
# (which is the sum of the number
# of students enrolled times the
# tuition fees for each university).

################  U name, students, fees
udacious_univs = [['Udacity',90000,0]]

usa_univs = [ ['California Institute of Technology',2175,37704],
              ['Harvard',19627,39849],
              ['Massachusetts Institute of Technology',10566,40732],
              ['Princeton',7802,37000],
              ['Rice',5879,35551],
              ['Stanford',19535,40569],
              ['Yale',11701,40500]  ]

def total_enrollment(p):
    students = 0
    fees = 0
#     print len(p)
#     print p
    
    for u_name, student, tuition in p:
#         print e
#         print e[0]
#         print e[1]
#         print e[2]
        students = students + student
        fees    = fees + student * tuition
    return students, fees
for e in usa_univs:
    print e
# print total_enrollment(udacious_univs)
#>>> (90000,0)

# The L is automatically added by Python to indicate a long
# number. If you are trying the question in an outside 
# interpreter you might not see it.
# print total_enrollment(usa_univs)
# >>> (77285,3058581079)
# end

# Investigating adding and appending to lists

# If you run the following four lines of codes, what are list1 and list2?

list1 = [1,2,3,4]
list2 = [1,2,3,4]

list1 = list1 + [5]
list2.append(5)

# to check, you can print them out using the print statements below.

# print list1
# print list2

# What is the difference between these two pieces of code?

def proc(mylist):
    mylist = mylist + [6]

def proc2(mylist):
    mylist.append(6)

def proc3(mylist):
    mylist += [7,8,9]

# Can you explain the results given by the four print statements below? Remove
# the hashes # and run the code to check.

# print list1
proc(list1)
# print list1

# print list2
proc2(list2)
# print list2

# Python has a special assignment syntax: +=.  Here is an example:

list3 = [1,2,3,4]
list3 += [5]

# Does this behave like list1 = list1 + [5] or list2.append(5)? Write a
# procedure, proc3 similar to proc and proc2, but for +=. When you've done
# that check your conclusion using the print-procedure call-print code as
# above.

# What happens when you try:

list1 = list1 + [7,8,9]
list2.append([7,8,9])
list3 += [7,8,9]

# print list3
proc3(list3)
# print list3
# When you've understood the difference between the three methods,
# write a procedure list_test which takes three lists as inputs. You should
# mutate the first input list to include 'a' as the last entry, mutate the
# second to include the entries 'a', 'b', 'c' and finally the last list should
# not be mutated but a copy should be returned with the additional entry 'w'.

def list_test(a, b, c):    
    # Your code here
    a.append('a')
    b += ['a', 'b', 'c']
    c = c + ['w']
    return c
#     pass # replace this line with your code



first_input = [1,2,3]
second_input = [4,5,6]
third_input = [7,8,9]

# print list_test(first_input, second_input, third_input)
#>>> [7,8,9,'w']
# print first_input
#>>> [1,2,3,'a']
# print second_input
#>>> [4,5,6,'a','b','c']
# print third_input
#>>> [7,8,9]

# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.
def symmetric(matrix):
    n = len(matrix)
    if n == 0:
        symmetric = True
    else:
        symmetric = False
    
    for e in matrix:
        if n == len(e):
            symmetric = True
        else:
            return False
    
    
    i = 0
    while i < n:
        j = 0
        row = []
        column = []
        while j < n:
            if i == j:
                row.append(matrix[i][j])
                column.append(matrix[i][j])
            else:
                row.append(matrix[i][j])
                column.append(matrix[j][i])
            j = j +1 
            if row == column:
                symmetric = True
            else:
                symmetric = False
        i = i +1
    return symmetric
            
# print symmetric([])

# print symmetric([[1, 2, 3],
#                 [2, 3, 4],
#                 [3, 4, 1]])
# #>>> True
# 
# print symmetric([["cat", "dog", "fish"],
#                 ["dog", "dog", "fish"],
#                 ["fish", "fish", "cat"]])
# #>>> True
# 
# print symmetric([["cat", "dog", "fish"],
#                 ["dog", "dog", "dog"],
#                 ["fish","fish","cat"]])
# #>>> False
# 
# print symmetric([[1, 2],
#                 [2, 1]])
# #>>> True
# 
# print symmetric([[1, 2, 3, 4],
#                 [2, 3, 4, 5],
#                 [3, 4, 5, 6]])
# #>>> False
# 
# print symmetric([[1,2,3],
#                 [2,3,1]])
# #>>> False


# The mean of a set of numbers is the sum of the numbers divided by the
# number of numbers. Write a procedure, mean, which takes a list of numbers
# as its input and return the mean of the numbers in the list.

# Hint: You will need to work out how to make your division into decimal
# division instead of integer division. You get decimal division if any of
# the numbers involved are decimals.

def list_mean(input):
    sum = 0.0
    for e in input:
        sum = sum + e
    return sum/len(input)
    

# print list_mean([1,2,3,4])
# #>>> 2.5
# print list_mean([1,3,4,5,2])
# #>>> 3.0
# #print list_mean([])
# #>>> ??? You decide. If you decide it should give an error, comment
# # out the print line above to prevent your code from being graded as
# # incorrect.
# print list_mean([2])
#>>> 2.0

# By Dimitris_GR from forums
# Modify Problem Set 31's (Optional) Symmetric Square to return True 
# if the given square is antisymmetric and False otherwise. 
# An nxn square is called antisymmetric if A[i][j]=-A[j][i] 
# for each i=0,1,...,n-1 and for each j=0,1,...,n-1.

def antisymmetric(A):
    n = len(A)
    if n == 0:
        anti_symmetric = True
    else:
        anti_symmetric = False
    
    for e in A:
        if n == len(e):
            anti_symmetric = True
        else:
            return False
        
    i = 0
    while i < n:
        j = 0
        row = []
        column = []
        while j < n:
            if A[i][j] == -1*A[j][i]:
                anti_symmetric = True
            else:
                anti_symmetric = False            
            j = j +1
        i = i +1
    return anti_symmetric


# Test Cases:

# print antisymmetric([[0, 1, 2], 
#                      [-1, 0, 3], 
#                      [-2, -3, 0]])   
#>>> True

# print antisymmetric([[0, 0, 0],
#                      [0, 0, 0],
#                      [0, 0, 0]])
#>>> True

# print antisymmetric([[0, 1, 2], 
#                      [-1, 0, -2], 
#                      [2, 2,  3]])
#>>> False

# print antisymmetric([[1, 2, 5],
#                      [0, 1, -9],
#                      [0, 0, 1]])
#>>> False
# By Ashwath from forums
# Given a list of lists representing a n * n matrix as input, 
# define a  procedure that returns True if the input is an identity matrix 
# and False otherwise.

# An IDENTITY matrix is a square matrix in which all the elements 
# on the principal/main diagonal are 1 and all the elements outside 
# the principal diagonal are 0. 
# (A square matrix is a matrix in which the number of rows 
# is equal to the number of columns)

def is_identity_matrix(matrix):
    n = len(matrix)
    if n == 0:
        identity = False
    else:
        identity = True
    
    for e in matrix:
        if n == len(e):
            identity = True
        else:
            return False
    
    
    i = 0
    while i < n:
        j = 0
        row = []
        column = []
        while j < n:
            if i == j:
                if 1 == matrix[i][j]:
                    identity = True
                else:
                    return False
            else:
                if 0 == matrix[i][j] and 0 == matrix[j][i]:
                    identity = True
                else:
                    return False
            j = j +1
        i = i +1
    return identity
    #Write your code here



# Test Cases:

# matrix1 = [[1,0,0,0],
#            [0,1,0,0],
#            [0,0,1,0],
#            [0,0,0,1]]
# print is_identity_matrix(matrix1)
# #>>>True
# 
# matrix2 = [[1,0,0],
#            [0,1,0],
#            [0,0,0]]
# 
# print is_identity_matrix(matrix2)
# #>>>False
# 
# matrix3 = [[2,0,0],
#            [0,2,0],
#            [0,0,2]]
# 
# print is_identity_matrix(matrix3)
# #>>>False
# 
# matrix4 = [[1,0,0,0],
#            [0,1,1,0],
#            [0,0,0,1]]
# 
# print is_identity_matrix(matrix4)
# #>>>False
# 
# matrix5 = [[1,0,0,0,0,0,0,0,0]]
# 
# print is_identity_matrix(matrix5)
# #>>>False
# 
# matrix6 = [[1,0,0,0],  
#            [0,1,0,2],  
#            [0,0,1,0],  
#            [0,0,0,1]]
# 
# print is_identity_matrix(matrix6)
# #>>>False
# 
# matrix7 = [[1, -1, 1],
#            [0, 1, 0],
#            [0, 0, 1]]
# print is_identity_matrix(matrix7)
# #>>>False   

        
# Numbers in lists by SeanMc from forums
# define a procedure that takes in a string of numbers from 1-9 and
# outputs a list with the following parameters:
# Every number in the string should be inserted into the list.
# If a number x in the string is less than or equal 
# to the preceding number y, the number x should be inserted 
# into a sublist. Continue adding the following numbers to the 
# sublist until reaching a number z that
# is greater than the number y. 
# Then add this number z to the normal list and continue.

#Hint - "int()" turns a string's element into a number

def numbers_in_lists(string):
    out = []
    sublist = []
    for i in string:
        if not len(out):
            out.append(int(i))
        elif int(i) > out[len(out)-1]:
            if len(sublist):
                out.append(sublist)
                sublist = []             
            out.append(int(i))                        
        else:            
            sublist.append(int(i))
    if len(sublist):
        out.append(sublist)                
#     print out
    return out

#testcases
# string = '543987'
# # numbers_in_lists(string)
# result = [5,[4,3],9,[8,7]]
# print repr(string), numbers_in_lists(string) == result
# string= '987654321'
# result = [9,[8,7,6,5,4,3,2,1]]
# print repr(string), numbers_in_lists(string) == result
# string = '455532123266'
# result = [4, 5, [5, 5, 3, 2, 1, 2, 3, 2], 6, [6]]
# print repr(string), numbers_in_lists(string) == result
# string = '123456789'
# result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print repr(string), numbers_in_lists(string) == result
# 
#            
# Crypto Analysis: Frequency Analysis
#
# To analyze encrypted messages, to find out information about the possible 
# algorithm or even language of the clear text message, one could perform 
# frequency analysis. This process could be described as simply counting 
# the number of times a certain symbol occurs in the given text. 
# For example:
# For the text "test" the frequency of 'e' is 1, 's' is 1 and 't' is 2.
#
# The input to the function will be an encrypted body of text that only contains 
# the lowercase letters a-z. 
# As output you should return a list of the normalized frequency 
# for each of the letters a-z. 
# The normalized frequency is simply the number of occurrences, i, 
# divided by the total number of characters in the message, n.

def freq_analysis(message):
    ##
    # Your code here
    ##
    freq_list = []
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    message_list = list(message)
    
    for e in alphabet:
        freq_list.append(1.0*message_list.count(e)/len(message_list))
    
    return freq_list



#Tests

print freq_analysis("abcd")
#>>> [0.25, 0.25, 0.25, 0.25, 0.0, ..., 0.0]

print freq_analysis("adca")
#>>> [0.5, 0.0, 0.25, 0.25, 0.0, ..., 0.0]

print freq_analysis('bewarethebunnies')
#>>> [0.0625, 0.125, 0.0, 0.0, ..., 0.0]
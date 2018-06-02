#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
'''
Created on 21/05/2018

@author: jruiz
You have a record of  students. Each record contains the student's name, and 
their percent marks in Maths, Physics and Chemistry. The marks can be floating 
values. The user enters some integer  followed by the names and marks for  
students. You are required to save the record in a dictionary data type. 
The user then enters a student's name. Output the average percentage marks 
obtained by that student, correct to two decimal places.

Example:
2
Harsh 25 26.5 28
Anurag 26 28 30
Harsh
'''

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        print(name)
        print(line)
        print(scores)
        student_marks[name] = scores
    query_name = input()
    if query_name in student_marks:
        if student_marks[query_name]:
            den = float(len(student_marks[query_name]))
            print(str.format("{0:.2f}",sum(student_marks[query_name])/den))
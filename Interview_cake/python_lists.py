'''
Created on 16/05/2018

@author: jruiz
'''
import re
'''
1 insert i e: Insert integer e at position .
2 print: Print the list.
3 remove e: Delete the first occurrence of integer .
4 append e: Insert integer  at the end of the list.
5 sort: Sort the list.
6 pop: Pop the last element from the list.
7 reverse: Reverse the list.
'''
def f1(lst, i, e):
    lst.insert(i, e)
    
def f2(lst):
    print(lst)
    
def f3(lst, e):
    if e in lst:
        lst.remove(e)
        
def f4(lst, e):
    lst.append(e)
    
def f5(lst):
    lst.sort()
    
def f6(lst):
    return lst.pop()

def f7(lst):
    lst.reverse()
    

def nested_list():
    """
    Given the names and grades for each student in a Physics class of  students,
    store them in a nested list and print the name(s) of any student(s) having 
    the second bigger grade.
    """
    physics = []
    result = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        physics.append([name, score])
    
    physics.sort(key = lambda x: x[1])
    
    big_ix = 0
    bigger = 0
    
    for i in range(0, len(physics)):
        if i == 0:
            big_ix = i
            bigger = physics[i][1]
        else:
            if physics[i][1] > bigger:
                bigger = physics[i][1]
                big_ix = i
                result.append(physics[i][0])
                break
    for i in range(big_ix + 1, len(physics)):
        if bigger in physics[i]:
            result.append(physics[i][0])
        elif physics[i][1] > bigger:
            break
    if result:
        result.sort()
        
    return result

if __name__ == '__main__':
    n = int(input())
    i = 0
    commands = []
    user_lst = []
    while i < n:
        commands.append(input())
        i += 1
    for e in commands:
        if re.search("insert", e):
            match = re.search("insert (\d+) (\d+)", e)
            f1(user_lst, int(match.group(1)), int(match.group(2)))
        elif re.search("print", e):
            f2(user_lst)
        elif re.search("remove", e):
            match = re.search("remove (\d+)", e)
            f3(user_lst, int(match.group(1)))
        elif re.search("append", e):
            match = re.search("append (\d+)", e)
            f4(user_lst, int(match.group(1)))
        elif re.search("sort", e):
            f5(user_lst)
        elif re.search("pop", e):
            f6(user_lst)
        elif re.search("reverse", e):
            f7(user_lst)    
        else:
            print("Invalid command...!!!")
            
    second = nested_list()
    for e in second:
        print(e)        

    
        
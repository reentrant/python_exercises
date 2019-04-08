#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
'''
 Write a function for reversing a linked list. ↴ Do it in place. ↴

Your function will have one input: the head of the list.

Your function should return the new head of the list.

Here's a sample linked list node class:

  class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next  = None

Gotchas

We can do this in O(1) space. So don't make a new list; use the existing list nodes!

We can do this is in O(n) time.

Careful—even the right approach will fail if done in the wrong order.

Try drawing a picture of a small linked list and running your function by hand. Does it actually work?

The most obvious edge cases are:

    the list has 0 elements
    the list has 1 element

Does your function correctly handle those cases?
Breakdown

Our first thought might be to build our reversed list "from the beginning," starting with the head of the final reversed linked list.

The head of the reversed list will be the tail of the input list. To get to that node we'll have to walk through the whole list once (O(n) time). And that's just to get started.

That seems inefficient. Can we reverse the list while making just one walk from head to tail of the input list?

We can reverse the list by changing the next pointer of each node. Where should each node's next pointer...point?

Each node's next pointer should point to the previous node.

How can we move each node's next pointer to its previous node in one pass from head to tail of our current list?


@author: Julian
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Solution():
    def insert(self, head_of_list, data):
        if head_of_list == None:
            head_of_list = Node(data)
        else:
            current = head_of_list
            while current.next:
                current = current.next
            current.next = Node(data)
        return head_of_list 
    
    def reverse(self, head):
        tail = current = head
        previous = None
        next_node = None
        if None == head or head.next == None:
            tail = head
        else:
            while current:
                next_node = current.next
                current.next = previous
                previous = current
                current = next_node
            tail = previous
        return tail
    
    def remove_duplicates(self,head_of_list):
        #Write your code here
        items = set()
        current = head_of_list
        previous = None
        while current:
            if current.data in items:
                # remove item
                temp = current
                previous.next = current = temp.next
                temp.next = None
                del temp
                continue
            else:
                items.add(current.data)
            previous = current
            current = current.next
        return head_of_list
    
    def display(self, head_node):
        current_node = head_node
        print('"', end='')
        while current_node:
            print(current_node.data, sep = '-', end='')
            current_node = current_node.next
        print('"')
        print(current_node)
    



if __name__ == '__main__':
    head_of_my_list = None
    my_list = Solution()
    my_list.display(head_of_my_list)

    print(type(my_list), my_list)
    number_of_elements = int(input())
    for _ in range(number_of_elements):
        data = input()
        head_of_my_list = my_list.insert(head_of_my_list, data)
        
    my_list.display(head_of_my_list)
    my_list.remove_duplicates(head_of_my_list)    
    my_list.display(head_of_my_list)
    tail = my_list.reverse(head_of_my_list)
    my_list.display(tail)
    my_list.display(head_of_my_list)
    my_list.display(tail)
    # my_list.display(tail)
    
        
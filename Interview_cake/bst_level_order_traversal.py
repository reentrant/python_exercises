'''
Created on 06/07/2018

@author: jruiz
Task 
A level-order traversal, also known as a breadth-first search, visits each level of a tree's nodes from left to right, top to bottom. You are given a pointer, , pointing to the root of a binary search tree. Complete the levelOrder function provided in your editor so that it prints the level-order traversal of the binary search tree.

Hint: You'll find a queue helpful in completing this challenge.

Input Format

The locked stub code in your editor reads the following inputs and assembles them into a BST: 
The first line contains an integer,  (the number of test cases). 
The  subsequent lines each contain an integer, , denoting the value of an element that must be added to the BST.

Output Format

Print the  value of each node in the tree's level-order traversal as a single line of  space-separated integers.

Sample Input

6
3
5
4
7
2
1
Sample Output

3 2 5 1 4 7 

'''
class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data
class Solution:
    
    height = 0
    
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root
    
    def level_order(self, root):
        queue = []
        if root != None:
            queue.append(root)
            while queue:
                #===============================================================
                # /*Dequeue node and make it temp_node*/
                #===============================================================
                root = queue.pop()
                print(root.data),
                #===============================================================
                # /*Enqueue left child */
                #===============================================================
                if root.left != None:
                    queue.insert(0, root.left)
                #===============================================================
                # /*Enqueue right child */    
                #===============================================================
                if root.right != None:
                    queue.insert(0, root.right)
                
if __name__ == '__main__':
    numbers = int(input())
    my_tree = Solution()
    root = None
    for _ in range (numbers):
        data = int(input())
        root = my_tree.insert(root, data)
    my_tree.level_order(root)

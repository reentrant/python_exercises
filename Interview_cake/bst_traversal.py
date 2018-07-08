'''
Created on 06/07/2018

@author: jruiz
Objective 
Today, we're working with Binary Search Trees (BSTs). 

ask 
The height of a binary search tree is the number of edges between the tree's root and its furthest leaf. You are given a pointer, , pointing to the root of a binary search tree. Complete the getHeight function provided in your editor so that it returns the height of the binary search tree.

Input Format

The locked stub code in your editor reads the following inputs and assembles them into a binary search tree: 
The first line contains an integer, , denoting the number of nodes in the tree. 
Each of the  subsequent lines contains an integer, , denoting the value of an element that must be added to the BST.

Output Format

The locked stub code in your editor will print the integer returned by your getHeight function denoting the height of the BST.

Sample Input

7
3
5
2
1
4
6
7

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
    
    def traverse(self, root):
        #Write your code here
        height = left = right = 0
        if root != None:
            if root.left != None:
                height = self.traverse(root.left) + 1
                left = height
            if root.right != None:
                height = self.traverse(root.right) + 1
                right = height
            Solution.height = max([Solution.height, left, right])

        else:
            print("Empty tree ", height)

        return height

    def getHeight(self, root):
        self.traverse(root)
        return Solution.height
    
     

if __name__ == '__main__':
    numbers = int(input())
    myTree = Solution()
    root = None
    for _ in range (numbers):
        data = int(input())
        root = myTree.insert(root, data)
    height = myTree.getHeight(root)
    print(height)
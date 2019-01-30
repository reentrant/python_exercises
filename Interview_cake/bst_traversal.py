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
                root.left = self.insert(root.left, data)
            else:
                root.right = self.insert(root.right, data)
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
            Solution.height = max(left, right)

        else:
            print("Empty tree ", height)

        return height

#     def getHeight(self, root):
#         self.traverse(root)
#         return Solution.height
    def getHeight(self, root):
        if root == None:
            return -1
        else:
            return 1 + max( self.getHeight(root.left), self.getHeight(root.right) )
        
    def contains(self, root, n):
        if root == None: return False
        if root.data == n:
            return True
        elif n < root.data:
            return self.contains(root.left, n)
        else:
            return self.contains(root.right, n)
        
    def print_inorder(self,root):
        if root.left != None:
            self.print_inorder(root.left)
        if root != None:
            print(root.data),
        if root.right != None:
            self.print_inorder(root.right)
            
    def print_preorder(self, root):
        if root != None:
            print(root.data),
        if root.left != None:
            self.print_preorder(root.left)
        if root.right != None:
            self.print_preorder(root.right)
            
    def print_postorder(self, root):
        if root.left != None:
            self.print_postorder(root.left)
        if root.right != None:
            self.print_postorder(root.right)
        if root != None:
            print(root.data),
            
    def print_levelorder(self, root):
        if root != None:
            queue = [root]
            while queue:
                node = queue.pop()
                print(node.data),
                if node.left != None:
                    queue.insert(0, node.left)
                if node.right != None:
                    queue.insert(0, node.right)
                
if __name__ == '__main__':
    numbers = int(raw_input())
    my_tree = Solution()
    root = None
    for _ in range (numbers):
        data = int(raw_input())
        root = my_tree.insert(root, data)
    height = my_tree.getHeight(root)
    print('height = ', height)
    print('tree contains 5?', my_tree.contains(root, 5))
    my_tree.print_inorder(root)
    print
    my_tree.print_preorder(root)
    print
    my_tree.print_postorder(root)
    print
    my_tree.print_levelorder(root)
    
    
    
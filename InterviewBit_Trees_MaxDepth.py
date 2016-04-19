from sys import stdin as Si

class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right= None

    def insert(self,b):
        if self.val:
            if b<self.val:
                if self.left is None:    self.left = TreeNode(b)
                else:   self.left.insert(b)
            elif b>self.val:
                if self.right is None:  self.right = TreeNode(b)
                else:   self.right.insert(b)
        else:
            self.val = b 

class Solution(object):
    def maxDepth(self, root):
        if root==None:
            return 0
        if root.left ==None and root.right==None:
            return 1
        l,r = 0,0
        if root.left is None:   return self.maxDepth(root.right)+1
        if root.right is None:  return self.maxDepth(root.left)+1
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1


                     
                
if __name__=='__main__':
    n = int(input())
    for i in range(n):
        c = list(map(int,Si.readline().split()))
        for i in range(len(c)):
            if i==0:
                Tree=TreeNode(c[i])
            else:
                Tree.insert(c[i])
        S = Solution()
        print (S.minDepth(Tree))

'''
Max Depth of Binary Tree

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the nearest leaf node.

    NOTE : The path has to end on a leaf node. 

Example :

         1
        /
       2

max depth = 2.

'''
        

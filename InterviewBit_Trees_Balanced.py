class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left=None
        self.right=None
        
    def insert(self,b):
        if self.val:    
            if b < self.val:
                if self.left is None:
                    self.left = TreeNode(b)
                else:
                    self.left.insert(b)
            elif b> self.val:
                if self.right is None:
                    self.right = TreeNode(b)
                else:
                    self.right.insert(b)
        else:
            self.val = b
            
class Solution:
    def isBalanced(self, A):
        return self.findHeight(A)>=0
        
    def findHeight(self, A):
        if A == None:
            return 0;
        lh = self.findHeight(A.left)
        rh = self.findHeight(A.right)
        #print (lh,rh)
        if lh<0 or rh<0 or abs(lh-rh)>1:    
            return -1
        return max(lh,rh)+1
    
if __name__=='__main__':
    n = int(input())
    for i in range(n):
        c = list(map(int,input().split(' ')))
        S = Solution()
        for i in range(len(c)):
            if i==0:
                Tree=TreeNode(c[i])
            else:
                Tree.insert(c[i])
        #Tree.Print()
        print (S.isBalanced(Tree))

  


'''


Given a binary tree, determine if it is height-balanced.

    Height-balanced binary tree : is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1. 

Return 0 / 1 ( 0 for false, 1 for true ) for this problem

Example :

Input : 
          1
         / \
        2   3

Return : True or 1 

Input 2 : 
         3
        /
       2
      /
     1

Return : False or 0 
         Because for the root node, left subtree has depth 2 and right subtree has depth 0. 
         Difference = 2 > 1. 

'''

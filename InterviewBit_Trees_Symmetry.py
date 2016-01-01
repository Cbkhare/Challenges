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
    def checkSym(self,L,R):
        if L and R:
            if L.val==R.val:
                return self.checksym(L.left,R.right) and self.checkSym(L.right,R.left)
            else:
                return False
        elif (L and not R) or (R and not L):
            return False
        else:
            return True
        
    def symSym(self,T):
        if T.left and T.right:
            return self.checkSym(T.left,T.right)
        else:
            return False 

'''


Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

Example :

    1
   / \
  2   2
 / \ / \
3  4 4  3

The above binary tree is symmetric.
But the following is not:

    1
   / \
  2   2
   \   \
   3    3

Return 0 / 1 ( 0 for false, 1 for true ) for this problem
'''

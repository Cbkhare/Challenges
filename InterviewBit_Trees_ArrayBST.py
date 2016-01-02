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
    def sortedArrayToBST(self, A):
        if len(A)==0:    return None   #base condition
        if len(A)%2==0: r = int(len(A)/2)-1
        else:   r=int(len(A)/2)
        #print (r,A,A[r])
        if r<0:    r=0
        root = TreeNode(A[r])
        root.left = self.sortedArrayToBST(A[:r])
        root.right = self.sortedArrayToBST(A[r+1:])

        return root 

            
    
'''
ARRAYBST

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

    Balanced tree : a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1. 

Example :


Given A : [1, 2, 3]
A height balanced BST  : 

      2
    /   \
   1     3

'''

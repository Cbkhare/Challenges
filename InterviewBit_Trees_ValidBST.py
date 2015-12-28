class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
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
            
    def Print(self):
        if self.left:
            self.left.Print()
        print(self.val)
        if self.right:
            self.right.Print()
        

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isValidBST(self, A):
        return self.isBST(A,float("-infinity"),float("infinity"))

    def isBST(self,root,min,max):    
        if root == None:
            return True
        if root.val<=min or root.val>=max:
            return False
        return self.isBST(root.left, min, root.val) and self.isBST(root.right, root.val, max)

        
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
        print (S.isValidBST(Tree))
        


'''
VALIDBST

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node’s key.
    The right subtree of a node contains only nodes with keys greater than the node’s key.
    Both the left and right subtrees must also be binary search trees.

Example :

Input : 
   1
  /  \
 2    3

Output : 0 or False


Input : 
  2
 / \
1   3

Output : 1 or True 

Return 0 / 1 ( 0 for false, 1 for true ) for this problem
'''

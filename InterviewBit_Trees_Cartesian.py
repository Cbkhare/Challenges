#############          TREES          ####################
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left=None
        self.right=None

class Solution:
    def whipMax(self,A):
        m = 0
        for i in range(1,len(A)):
            if A[i]>A[m]:
                m = i
        return m

    def buildTree(self, A):
        
        if A==[]:     return None
        ind = self.whipMax(A)
        Node = TreeNode(A[ind])
        Node.left = self.buildTree(A[:ind])
        Node.right = self.buildTree(A[ind+1:])
        return Node
                           


if __name__=='__main__':
    n = int(input())
    for i in range(n):
        c = list(map(int,input().split(' ')))
        S = Solution()
        print (S.buildTree(c))




'''


Given an inorder traversal of a cartesian tree, construct the tree.

    Cartesian tree : is a heap ordered binary tree, where the root is greater than all the elements in the subtree. 

    Note: You may assume that duplicates do not exist in the tree. 

Example :

Input : [1 2 3]

Return :   
          3
         /
        2
       /
      1

'''

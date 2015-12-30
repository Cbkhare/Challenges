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
        
class Solution:
    # @param A : root node of tree
    # @return an integer
    def findN(self,A,n,P):
        '''
        ####----Recursive----####
        if n<A.val and A.left:
            P = A
            return self.findN(A.left,n,P)
        elif n>A.val and A.right:   return self.findN(A.right,n,P)
        elif n==A.val:
            return A,P
        '''
        ####----Non-Recursive----####
        while n!=A.val:
            if n<A.val and A.left:
                P = A           #Stores last Parent greater than n 
                A= A.left
            elif n>A.val and A.right:
                A = A.right
            elif n==A.val:
                break
            
        return A,P
            
                
    def getSuccessor(self,A,n):
        node,P = self.findN(A,n,P=None)
        if node.right ==None:
            return P.val        #return P
        else:
            #print('check, i m here')
            node = node.right
            while node.left!=None:
                node = node.left
            return node.val     #return node
        
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
        c1 = int(input())
        print (S.inOrderNext(Tree,c1))
  


'''
Given a BST node, return the node which has value just greater than the given node.

Example:

Given the tree

               100
              /   \
            98    102
           /  \
         96    99
          \
           97

Given 97, you should return the node corresponding to 98 as thats the value just greater than 97 in the tree.
If there are no successor in the tree ( the value is the largest in the tree, return NULL).

Using recursion is not allowed.

Assume that the value is always present in the tree.

PROBLEM APPROACH:

Complete solution in the hint.
'''

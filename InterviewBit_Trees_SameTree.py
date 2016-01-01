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
    def isSameTree(self,T1,T2):
        if T1==None and T2==None:   return True
        elif (T1!=None and T2==None) or (T2==None and T2!=None):
            return False
        if T1.val!=T2.val:  return False
        else:
            return self.isSameTree(T1.left,T2.left) and self.isSameTree(T1.right,T2.right)

            
    
if __name__=='__main__':
    n = int(input())
    def sinsert(c):
        for i in range(len(c)):
            if i==0:
                Tree=TreeNode(c[i])
            else:
                Tree.insert(c[i])
        return Tree
    for i in range(n):
        T1 = sinsert(list(map(int,input().split(' '))))
        T2 = sinsert(list(map(int,input().split(' '))))
        S = Solution()
        print (S.checkEqual(T1,T2))

  


'''
SAMETREE

Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem

Example :

Input : 

   1       1
  / \     / \
 2   3   2   3

Output : 
  1 or True

'''

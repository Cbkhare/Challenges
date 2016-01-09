#############          TREES          ####################
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
    def treeLST(self,N):
        if N.left:
            self.treeLST(N.left)
        self.B.append(N.val)
        if N.right:
            self.treeLST(N.right)
    
    def t2Sum(self, A,K):
        self.B=[]
        self.treeLST(A)
        i,j=0,len(self.B)-1
        while i<j:
            if self.B[i]+self.B[j]==K:
                return True
            elif self.B[i]+self.B[j]>K:
                j-=1
            elif self.B[i]+self.B[j]<K:
                i+=1
        return False
        
    
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
        c = int(input())
        S = Solution()
        print (S.t2Sum(T1,c))




'''
T2SUM

Given a binary search tree T, where each node contains a positive integer, and an integer K, you have to find whether or not there exist two different nodes A and B such that A.value + B.value = K.

Return 1 to denote that two such nodes exist. Return 0, otherwise.

Notes
- Your solution should run in linear time and not take memory more than O(height of T).
- Assume all values in BST are distinct.

Example :

Input 1: 

T :       10
         / \
        9   20

K = 19

Return: 1

Input 2: 

T:        10
         / \
        9   20

K = 40

Return: 0

'''

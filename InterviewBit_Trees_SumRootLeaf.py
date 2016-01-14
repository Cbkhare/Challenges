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

class Solution(object):
    def whip(self,T, A):
        #print (A.val, T,self.List)
        if not A.left and not A.right:
            self.List.append(int(T+str(A.val)))
            return 
        T +=str(A.val)
        if A.left:
            self.whip(T, A.left)
        if A.right:
            self.whip(T, A.right)
        T = T[:-1]

    def sumNumbers(self, N):
        if N==None:     return 0
        self.List = []
        T = ''
        self.whip(T,N)
        return sum(self.List)


if __name__=='__main__':
    
    print ('Note: Data Strucutre used here is BST')
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
        S = Solution()
        print (S.sumNumbers(T1))




'''
Sum Root to Leaf Numbers 
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3

The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.
'''

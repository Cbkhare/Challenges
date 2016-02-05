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
    def checkSum(self,N,Sum):
        if N==None: return False
        Sum+=N.val
        if N.left==None and N.right==None:
            if bool(Sum==self.s):
                return True
            else:
                return False
        #print (Sum)
        if N.left!=None or N.right!=None:
            return (self.checkSum(N.left,Sum) or self.checkSum(N.right,Sum))
        else:
            Sum-=N.val


    def hasPathSum(self,N,s):
        Sum = 0
        self.s = s
        return self.checkSum(N,Sum)
        


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
        S = Solution()
        c = int(input())
        print (S.hasPathSum(T1,c))




'''
Path Sum

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
For example:
Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1

return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
'''

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
    def checkSum(self,N,st):
        if N==None: return
        st.append(N.val)
        print (st)
        if N.left==None and N.right==None:
            print (sum(st),self.s)
            if sum(st)==self.s:
                self.final_st.append([i for i in st])
        if N.left:
            self.checkSum(N.left,st)
        if N.right:
            self.checkSum(N.right,st)
        st.pop(-1)


    def pathSum(self,N,s):
        st= []
        self.final_st = [] 
        self.s = s
        self.checkSum(N,st)
        return self.final_st
        


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
        print (S.pathSum(T1,c))




'''


Given a binary tree and a sum, find all root-to-leaf paths where each path’s sum equals the given sum.

For example:
Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1

return

[
   [5,4,11,2],
   [5,8,4,5]
]

'''

from sys import stdin as Si, maxsize as m
from math import factorial as F
import collections 
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
        
class Solution:
    def bazinga(self,s,e):
        if s>e: return [None]
        result = []
        for rootVal in range(s,e+1):
            left = self.bazinga(s,rootVal-1)
            right = self.bazinga(rootVal+1,e)

            for l in left:
                for r in right:
                    root = TreeNode(rootVal)
                    root.left = l
                    root.right = r
                    result.append(root)
        return result 
        
    def generateTrees(self,A):
        return self.bazinga(1,A)
        




if __name__=='__main__':
    S=Solution()
    for i in range(int(Si.readline())):
        print (S.generateTrees(int(Si.readline())))

'''


Given A, generate all structurally unique BST’s (binary search trees) that store values 1...A.

Example :
Given A = 3, your program should return all 5 unique BST’s shown below.


   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

'''

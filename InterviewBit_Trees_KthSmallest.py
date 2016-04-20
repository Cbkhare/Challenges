from sys import stdin as Si

class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right= None

    def insert(self,b):
        if self.val:
            if b<self.val:
                if self.left is None:    self.left = TreeNode(b)
                else:   self.left.insert(b)
            elif b>self.val:
                if self.right is None:  self.right = TreeNode(b)
                else:   self.right.insert(b)
        else:
            self.val = b 


class Solution:
    # @param A : integer
    # @return a list of TreeNode
    def __init__(self):
        self.q = []
        
    def kthSmallest(self,R,k):
        #checking left 
        if R.left!=None:    self.kthSmallest(R.left,k)
        if R.val not in self.q and len(self.q)<k:
            self.q.append(R.val)
        #adding root
        if len(self.q)==k:  return self.q[-1]
        #moving right
        print(R.val,self.q)
        if R.right:  return self.kthSmallest(R.right,k)
        else:
            return 

                     
                
if __name__=='__main__':
    n = int(input())
    for i in range(n):
        c = list(map(int,Si.readline().split()))
        for i in range(len(c)):
            if i==0:
                Tree=TreeNode(c[i])
            else:
                Tree.insert(c[i])
        S = Solution()
        k = int(Si.readline())
        print (S.kthSmallest(Tree,k))
        
'''
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

Hint:

    Try to utilize the property of a BST.
    What if you could modify the BST node's structure?
    The optimal runtime complexity is O(height of BST).


Example :

Input : 
  2
 / \
1   3

and k = 2

Return : 2

As 2 is the second smallest element in the tree.

    NOTE : You may assume 1 <= k <= Total number of nodes in BST 



'''

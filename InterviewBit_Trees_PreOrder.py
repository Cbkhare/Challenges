class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def preOrder(self, A):
        self.List.append(A.val)
        if A.left:   self.preOrder(A.left)
        if A.right:  self.preOrder(A.right)

    def preorderTraversal(self, A):
        self.List = []
        self.preOrder(A)
        return self.List
'''
PREORDER

Given a binary tree, return the postorder traversal of its nodes’ values.

Example :

Given binary tree

   1
    \
     2
    /
   3

return [1,2,3].

Using recursion is not allowed.
'''

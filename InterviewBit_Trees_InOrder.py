class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inOrder(self, A):
        if A.left:   self.inOrder(A.left)
        self.List.append(A.val)
        if A.right:  self.inOrder(A.right)

    def inorderTraversal(self, A):
        self.List = []
        self.inOrder(A)
        return self.List
'''
INORDER

Given a binary tree, return the postorder traversal of its nodes’ values.

Example :

Given binary tree

   1
    \
     2
    /
   3

return [1,3,2].

Using recursion is not allowed.
'''

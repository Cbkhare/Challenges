class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def postOrder(self, A):
        if A.left:   self.postOrder(A.left)
        if A.right:  self.postOrder(A.right)
        self.List.append(A.val)

    def postorderTraversal(self, A):
        self.List = []
        self.postOrder(A)
        return self.List
'''
POSTORDER

Given a binary tree, return the postorder traversal of its nodes’ values.

Example :

Given binary tree

   1
    \
     2
    /
   3

return [3,2,1].

Using recursion is not allowed.
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
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

    def preOrder(self):
        print(self.val)         #root
        if self.left:   self.left.preOrder()
        if self.right:  self.right.preOrder()

    def inOrder(self):
        if self.left:   self.left.inOrder()
        print(self.val)     #root
        if self.right:  self.right.inOrder()

    def postOrder(self):
        if self.left:   self.left.postOrder()
        if self.right:  self.right.postOrder()
        print(self.val)     #root
        
        
if __name__=='__main__':
    n = int(input())
    for i in range(n):
        c = list(map(int,input().split(' ')))
        for i in range(len(c)):
            if i==0:
                Tree=TreeNode(c[i])
            else:
                Tree.insert(c[i])
        print ('++++++PreOrder++++++')
        Tree.preOrder()
        print('++++++InOrder++++++')
        Tree.inOrder()
        print('++++++PostOrder++++++')
        Tree.postOrder()
        
        


'''
###############---RESULT---###############
    4
   / \
  2   5
 / \
1   3
++++++PreOrder++++++
4
2
1
3
5
++++++InOrder++++++
1
2
3
4
5
++++++PostOrder++++++
1
3
2
5
4

##################################
4 2 1 3 7 6 8 5
     4
   /   \
  2     7
 / \   / \ 
1   3 6   8
     /
    5
++++++PreOrder++++++
4
2
1
3
7
6
5
8
++++++InOrder++++++
1
2
3
4
5
6
7
8
++++++PostOrder++++++
1
3
2
5
6
8
7
4
'''

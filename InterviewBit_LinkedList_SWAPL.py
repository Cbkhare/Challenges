class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, A):
        if A.next==None or A==None:  return A
        current = A
        while current !=None and current.next!=None:
            old = current.val
            current.val = current.next.val
            current.next.val= old
            current = current.next.next
        return A 
                
            
if __name__=='__main__':
    n = int(input())
    for i in range(n):
        Head = ListNode(-1)
        B = Head
        c = list(map(int,input().split(' ')))
        for i in c:
            B.next = ListNode(i)
            B = B.next
        S = Solution()
        sol = (S.swapPairs(Head.next))
        while sol!=None:
            print (sol.val)
            sol=sol.next
      


'''
SWAPL

Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
'''

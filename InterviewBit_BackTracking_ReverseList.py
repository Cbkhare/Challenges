# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    head = ListNode(-1)
    def reverseList(self, A):
        if A.next==None:
            self.head.next = A
            return self.head.next
        self.reverseList(A.next)
        B =A.next
        B.next= A
        A.next = None
        return self.head.next

        
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
        sol= (S.reverseList(Head.next))
        while sol!=None:
            print (sol.val)
            sol=sol.next


'''


Reverse a linked list using recursion.

Example :
Given 1->2->3->4->5->NULL,

return 5->4->3->2->1->NULL.
'''

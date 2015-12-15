#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        current = A 
        if current.next==None:
            return current
        while current!= None and current.next!=None:
            if current.val==current.next.val:
                current.next=current.next.next
            else:   current = current.next
        return A 

        
if __name__=='__main__':
    n = int(input())
    for i in range(n):
        c = list(map(int,input().split(' ')))
        Head = ListNode(-1)
        B = Head
        for i in c:
            B.next = ListNode(i)
            B = B.next
        S = Solution()
        sol = S.deleteDuplicates(Head.next)
        while sol!=None:
            print (sol.val)
            sol=sol.next
        

'''


Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
'''

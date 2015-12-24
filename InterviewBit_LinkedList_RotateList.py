# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def rotateRight(self, A, B):
        if A.next==None or B==0:    return A
        
        head = ListNode(-1)
        head.next = A
        last = None
        lngth = 0 
        while A!=None:
            last = A
            A=A.next
            lngth +=1
        B = B%lngth
        if B==0:    return head.next
        else:
            current=head.next
            A = current 
            pos = 0
            while pos < lngth-B-1:
                current = current.next 
                pos+=1
            last.next = head.next
            A = current.next
            current.next = None 
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
        c1 = int(input())
        sol =  (S.rotateRight(Head.next,c1))
        while sol!=None:
            print (sol.val)
            sol=sol.next

      


'''
ROTATELIST

Given a list, rotate the list to the right by k places, where k is non-negative.

For example:

Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
'''

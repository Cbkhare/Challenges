# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    old = None
    repeat = False
    def deleteDuplicates(self, A):
        if A.next==None:
            return A
        else:
            current = A
            old = None
            repeat = False
            while current!=None and current.next!=None:
                if current.val==current.next.val:
                    repeat = True 
                else:
                    if repeat and old ==None:    #1 1 1 2 2 2 3
                        A = current.next
                    elif repeat and old!=None:   #1 2 2 2 3
                        old.next = current.next
                    elif repeat == False:        #1 2 3
                        old = current
                    repeat = False
                current = current.next 
            if repeat:
                if old ==None: return None       #1 1 1 2 2 2 or 1 1 1 1
                else:   old.next=None            #1 2 3 3 3
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
        sol= (S.deleteDuplicates(Head.next))
        while sol!=None:
            print (sol.val)
            sol=sol.next


'''
REMDUPLNK2

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
'''

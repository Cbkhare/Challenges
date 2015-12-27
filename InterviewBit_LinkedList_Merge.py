# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        if A.val<=B.val:
            head = A
        else:
            head = B
        current = ListNode(-1)
        while A!= None and B!=None:
            #print (A.val,B.val)
            if A.val<B.val:
                current.next = A
                A = A.next
                current = current.next
            elif A.val>B.val:
                current.next = B
                B = B.next
                current = current.next
            elif A.val==B.val:
                current.next = A
                current=current.next
                A = A.next
                current.next = B
                current = current.next
                B = B.next
            
        if A!=None:
            current.next = A
        else:
            current.next = B 
        return head
            
        
    
if __name__=='__main__':
    n = int(input())
    for i in range(n):
        Head = ListNode(-1)
        B = Head
        c = list(map(int,input().split(' ')))
        for i in c:
            B.next = ListNode(i)
            B = B.next
        Head1 = ListNode(-1)
        B1 = Head1
        c1 = list(map(int,input().split(' ')))
        for j in c1:
            B1.next = ListNode(j)
            B1 = B1.next
        S = Solution()
        sol = (S.mergeTwoLists(Head.next,Head1.next))
        while sol!=None:
            print (sol.val)
            sol=sol.next


'''
MERGE

Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists, and should also be sorted.

For example, given following linked lists :

  5 -> 8 -> 20 
  4 -> 11 -> 15

The merged list should be :

4 -> 5 -> 8 -> 11 -> 15 -> 20

'''

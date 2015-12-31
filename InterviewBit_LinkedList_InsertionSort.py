class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def insertionSortList(self, A):
        head= ListNode(-1)
        current = head.next 
        while A!=None:
            if current==None:
                head.next=ListNode(A.val)
                current = head.next
            else:
                old = None
                c = head.next
                while A.val>c.val:
                    old = c
                    c=c.next
                    if c==None: break
                if old==None:   #first element
                    t = head.next
                    head.next=ListNode(A.val)
                    head.next.next=t                    
                else:
                    current = ListNode(A.val)
                    old.next = current 
                    current.next = c
            A=A.next
        return head.next
                    
                    
            
        
            
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
        sol =  (S.insertionSortList(Head.next))
        while sol!=None:
            print (sol.val)
            sol=sol.next
        


'''
INSERTIONSORT

Sort a linked list using insertion sort.

We have explained Insertion Sort at Slide 7 of Arrays

Insertion Sort Wiki has some details on Insertion Sort as well.

Example :

Input : 1 -> 3 -> 2

Return 1 -> 2 -> 3
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def partition(self, A, B):
        h1 = ListNode(-1)
        p1 = h1
        h2 = ListNode(-1)
        p2 = h2
        while A !=None:
            if A.val<B:
                p1.next = ListNode(A.val)
                p1 = p1.next
            else:
                p2.next = ListNode(A.val)
                p2 = p2.next
            A = A.next
        p1.next = h2.next 
        return h1.next
        
if __name__=='__main__':
    n = int(input())
    for i in range(n):
        S = Solution()
        c = list(map(int,input().split(' ')))
        Head = ListNode(-1)
        B = Head
        for i in c:
            B.next = ListNode(i)
            B = B.next
        c1 = int(input())
        result =  (S.partition(Head.next,c1))
        c =[]
        while result!=None:
            c+=[result.val]
            result = result.next
        print (c)
        

'''
PARTITIONLIST

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
'''

#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param m : integer
    # @param n : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, m, n):
        if A==None or A.next==None: return A
        head = ListNode(-1)
        current = ListNode(0)
        head.next = A #current
        count = 1
        prev = None 
        while A.next!=None:# and A!=None:
            if count ==m:
                old = None 
                while count<=n:
                    C = A.next
                    temp = A.next
                    A.next = old
                    old = A
                    count+=1
                    if count <= n:
                        A = temp
                if prev!= None: prev.next = A
                else:   head.next = A
                while A.next!=None:
                    #print (A.val,'-')
                    A=A.next
                A.next = C
                break
            else:
                prev = A 
                A=A.next
                count+=1
        return  head.next
                
          
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
        m,n = list(map(int,input().split(' ')))
        sol = (S.reverseBetween(Head.next,m,n))
        while sol!=None:
            print (sol.val)
            sol=sol.next

      


'''
REVERSELIST

Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

    Note:
    Given m, n satisfy the following condition:
    1 ≤ m ≤ n ≤ length of list.

    Note 2:
    Usually the version often seen in the interviews is reversing the whole linked list which is obviously an easier version of this question. 

'''

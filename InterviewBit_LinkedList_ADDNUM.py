class Node:
    def __init__(self,data,nxt=None):     #by default None 
        self.data = data
        self.next = None
    
    def __str__(self):
        return ('Node['+str(self.data)+']')
    
    
class Linked_List:
    def __init__(self):
        self.head = None                      #by default None

    def insert(self,data):
        if self.head==None:                   #i.e there is no element in the list
            self.head = Node(data)
        else:
            current = self.head               #point to begining
            while current.next != None :
                current = current.next
            current.next = Node(data)
        #return (self.)


    def get(self,position):
        if self.head==None:
            return ('Linked List Empty')
        else:
            x = 0
            current = self.head
            while current.next != None:
                if x == position:
                    return current
                else:
                    x+=1
                    current = current.next
            if position - x >0:
                return ('Element not in the LinkedList')
            else:
                return current
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def reverse(self,N):
        L = N 
        old = None 
        while L.next!=None:
            temp = L.next
            L.next = old
            old = L
            L = temp
        L.next = old
        return L
    def string(self,S):
        S = self.reverse(S)
        s = ''
        while S.next!=None:
            s+= str(S.data)
            S = S.next
        s += str(S.data)
        return s
        
    def addTwoNumbers(self, A, B):
        n1,n2 ='',''

        n1 = self.string(A)
        n2 = self.string(B)
        print (int(n1)+int(n2))
        n = str(int(n1)+int(n2))
        for x in range(len(str(n))):
            if x==0:
                L = ListNode(int(n[x]))
                current = L
            else:
                #current and L has already been intialized above clause 
                current.next = ListNode(int(n[x]))
                current = current.next
        L = self.reverse(L)
        while L.next!=None:
            print (L.val)
            L=L.next
        return (L.val)

            
        
if __name__=='__main__':
    n = int(input())
    for i in range(n):
        B = Linked_List()
        C = Linked_List()
        strng1 = list(map(int,input().split(' ')))
        strng2 = list(map(int,input().split(' ')))
        for j in range(len(strng1)):
            ('Insert- ',B.insert(strng1[j]))
        for j in range(len(strng2)):
            ('Insert- ',C.insert(strng2[j]))
        S = Solution()
        print (S.addTwoNumbers(B.get(0),C.get(0)))


'''


You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

    342 + 465 = 807

Make sure there are no trailing zeros in the output list
So, 7 -> 0 -> 8 -> 0 is not a valid response even though the value is still 807.

'''

class Node:
    def __init__(self,data=None,nxt=None):     #by default None 
        self.data = data
        self.nxt = nxt
    def __str__(self):
        return ('Node[Data='+str(self.data)+']')
    
class Linked_List:
    def __init__(self):
        self.head = None                      #by default None

    def insert(self,data):
        if self.head==None:                   #i.e there is no element in the list
            self.head = Node(data)
        else:
            current = self.head               #point to begining
            while current.nxt != None :
                current = current.nxt
            current.nxt = Node(data)
        return (self.display())
            
    def get(self,position):
        if self.head==None:
            return ('Linked List Empty')
        else:
            x = 0
            current = self.head
            while current.nxt != None:
                if x == position:
                    return current
                else:
                    x+=1
                    current = current.nxt
            if position - x >0:
                return ('Element not in the LinkedList')
            else:
                return current

    def display(self):
        if self.head==None:
            return ('Linked List Empty')
        else:
            current = self.head
            Link_list= str(current)     #instantiated with head
            while current.nxt!=None:
                current = current.nxt
                Link_list += str(current)
            return (Link_list)
    
class Solution:
    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, A):
        T = A
        s=''
        while A.nxt!=None:
            s+=str(A.data)
            A=A.nxt
        s+=str(A.data)   #(final value)
        #reversing
        old = None
        while T.nxt!=None:
            temp = T.nxt 
            T.nxt= old
            old = T
            T =temp
        T.nxt = old
        rs =''
        while T.nxt!=None:
            rs+=str(T.data)
            T=T.nxt
        rs+=str(T.data)

        if s==rs:
            return 'Palindrome'
        else:
            return 'Not Palindrome'
        
              
if __name__=='__main__':
    n = int(input())
    for i in range(n):
        strng = input()
        B = Linked_List()
        for j in range(len(strng)):
            (B.insert(strng[j]))
        S = Solution()
        print (S.lPalin(B.get(0)))

'''
LPALIN

Given a singly linked list, determine if its a palindrome. Return 1 or 0 denoting if its a palindrome or not, respectively.

Notes:
- Expected solution is linear in time and constant in space.

For example,

List 1-->2-->1 is a palindrome.
List 1-->2-->3 is not a palindrome.

'''

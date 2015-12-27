class Node:
    def __init__(self,data,nxt=None):     #by default None 
        self.data = data
        self.nxt = None
    
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
            while current.nxt != None :
                current = current.nxt
            current.nxt = Node(data)
        return (self.display())
    
    def delete(self,Head,count):
        if self.head==None:
            return ('Linked List Empty')
        else:
            
            if count ==1:
                start=Head.nxt
                Head.nxt = None
                return start
            
            start = Head
            found = False
            current = Head
            old_current = ''
            while current.nxt!= None and not found:
                count-=1
                if count ==0:
                    found = True
                    break
                else:
                    old_current = current
                    current = current.nxt
            if found:
                old_current.nxt = current.nxt
                return(start)
            else:
                old_current.nxt = None
                return ('Element does not exist')
            
                
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

    def reverse(self):
        if self.head==None:
            return ('Linked List Empty')
        else:
            current = self.head
            old = None
            while current.nxt !=None:
                temp = current.nxt
                current.nxt = old 
                old = current
                current = temp
            current.nxt = old
            return current 

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
            
class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def reverse(self,Head):
        if Head==None:
            return ('None')
        else:
            current = Head
            old = None
            while current.nxt !=None:
                temp = current.nxt
                current.nxt = old 
                old = current
                current = temp
            current.nxt = old
            return current
        
    def delete(self,Head,count):
        if count ==0:
            return (Head)
        else:
            
            if count ==1:
                if Head.nxt==None:
                    return None
                else:
                    start=Head.nxt
                    Head.nxt = None
                    return start
            
            start = Head
            found = False
            current = Head
            old_current = current
            while current.nxt!= None and not found:
                count -=1
                if count ==0:
                    found = True
                    break
                else:
                    old_current = current
                    current = current.nxt
            print (found)
            if found:
                old_current.nxt = current.nxt
                current.nxt=None
                return(start)
            else:
                old_current.nxt = None
                return (start)
            
    def display(self,Head):
        if Head==None:
            return ('Linked List Empty')
        else:
            current = Head
            Link_list= str(current)     #instantiated with head
            while current.nxt!=None:
                current = current.nxt
                Link_list += str(current)
            return (Link_list)
            
    def removeNthFromEnd(self, A, B):
        Last_Node = self.reverse(A)
        
        N = self.delete(Last_Node,B)
        N = self.reverse(N)
        if N!='None':
            return (print (self.display(N)))
        else:
            return []

        
if __name__=='__main__':
    n = int(input())
    for i in range(n):
        B = Linked_List()
        strng = list(map(int,input().split(' ')))
        node = int(input())
        for j in range(len(strng)):
            print ('Insert- ',B.insert(strng[j]))
        S = Solution()
        print (S.removeNthFromEnd(B.get(0),node))


'''
NTHEND

Given a linked list, remove the nth node from the end of list and return its head.

For example,
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.

    Note:
    * If n is greater than the size of the list, remove the first node of the list. 

Try doing it using constant additional space.

'''

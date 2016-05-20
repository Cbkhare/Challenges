from sys import stdin as Si, maxsize as m
from math import factorial as F,log as lg 
from  collections import Counter as C 
from operator import itemgetter as ig 
import heapq as H 

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
        
class Solution:

    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self,L):
        if L==[]:   return None
        else:
            heap = [] 
            for l in L:
                while l!=None:
                    heap.append(l.val)
                    l=l.next
            H.heapify(heap)

            head = ListNode(0);curr = head
            for h in heap:
                p = H.heappop(heap)
                curr.next = ListNode(p.val)
                curr = curr.next
            return head.next 

'''
Merge K Sorted Lists

Merge k sorted linked lists and return it as one sorted list.

Example :

1 -> 10 -> 20
4 -> 11 -> 13
3 -> 8 -> 9

will result in

1 -> 3 -> 4 -> 8 -> 9 -> 10 -> 11 -> 13 -> 20

'''

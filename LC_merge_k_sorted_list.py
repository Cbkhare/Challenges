from heapq import heappush, heappop, heapify

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        x = []
        heapify(x)
        for node in lists:
            while node:
                heappush(x,node.val)
                node = node.next
        l = len(x)
        head = None
        curr = None
        for i in range(l):
            n = ListNode(heappop(x))
            if i==0:
                head = n
                curr = n
            else:
                curr.next = n
                curr = curr.next
        return head
                

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def maxone(self, A, B):
        n = len(A)
        left = 0
        right = 0
        noZerosInWindow = 0
        if A[right] == 0:
            noZerosInWindow += 1
        bestLeft = 0
        bestRight = 0
        
        while right < n:
            if noZerosInWindow <= B:
                right += 1
                if right < n and A[right] == 0:
                    noZerosInWindow += 1
            if noZerosInWindow > B:
                if A[left] == 0:
                    noZerosInWindow -= 1
                left += 1
            
            if right >= n:
                if n - 1 - left > bestRight - bestLeft:
                    bestLeft = left
                    bestRight = n - 1
            elif right - left > bestRight - bestLeft:
                bestLeft = left
                bestRight = right
            #print bestLeft, bestRight
        if bestRight > n - 1:
            bestRight = n - 1
        return [s for s in range(bestLeft, bestRight+1)]
                    
        
if __name__=='__main__':
    n = int(input())
    for i in range(n):
        #B = Linked_List()
        #C = Linked_List()
        #strng1 = list(map(int,input().split(' ')))
        #strng2 = list(map(int,input().split(' ')))
        #for j in range(len(strng1)):
        #    ('Insert- ',B.insert(strng1[j]))
        #for j in range(len(strng2)):
        #    ('Insert- ',C.insert(strng2[j]))
        S = Solution()
        c = list(map(int,input().split(' ')))
        c1 = int(input())
        print (S.maxone(c,c1))


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

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def inside_stack(self):
        pass
    def trap(self, A):
        '''
        if len(A)<=2:   return 0
        i = 0
        lp = 0
        rp = 1
        stack = []
        while i<len(A)-1:
            pass
        '''
        n = len(A)
        if n <= 2:
            return 0
        left = [0]* n
        right = [0] * n
        Max = A[0]
        left[0] = A[0]
        for i in range(1, n) :
            if A[i] < Max :
                left[i] = Max

            else :
                left[i] = A[i]
                Max = A[i]
        Max = A[n-1]
        right[n-1] = Max
        for i in range(n -2, -1, -1) :
            if A[i] < Max :
                right[i] = Max
            else :
                right[i] = A[i]
                Max = A[i]
        water = 0
        for i in range(n) :
            water +=  min( left[i], right[i]) - A[i]
        return water
            
            
    
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
        #c = input()
        print (S.trap(c))


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

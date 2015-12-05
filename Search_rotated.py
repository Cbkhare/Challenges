class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def binary(self,A,B):
        x = 0
        s,e= 0,len(A)-1
        while s<=e:
                m = s+int((e-s)/2)
                if A[m]==B:
                    x = m
                    e = m-1
                elif A[m]>B:
                    e = m-1 
                elif A[m]<B:
                    s = m+1
        return x 
        
    def search(self, A,B):
        s,e= 0,len(A)-1
        if A[0]==B: return 0
        #finding the min element
        m = 0
        while A[s]>A[e]:
            m = s + int((e-s)/2)
            #print (s,e,m)
            if A[s]<A[m]:
                s = m+1
            elif A[m]<=A[s]:
                e= m
        m = m+1        #since above while loops runs for mor than one time 
        #print (s,e,m,A[m])
        
        if A[m]==B: return m
        if B in A[:m+1]:
            #print (A[:m])
            return self.binary(A[:m],B)
        elif B in A[m+1:]:
            #print (A[m+1:])
            return m+self.binary(A[m:],B)
        else:
            return -1
    
if __name__=='__main__':
    B = Solution()
    n = int(input())
    c  = tuple(map(int,input().split(' ')))
    for i in range(n):
        #c  = tuple(map(int,input().split(' ')))
        m = int(input())
        print (B.search(c,m))
    

'''


Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2 ).

You are given a target value to search. If found in the array, return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Input : [4 5 6 7 0 1 2] and target = 4
Output : 0

        NOTE : Think about the case when there are duplicates. Does your current solution work? How does the time complexity change?*

Ex:
4 5 5 0 0 0 1
0
3

4 5 5 6 7 0 0 1
0
5
5
1
4
0
6 
3
7
4
1
'''

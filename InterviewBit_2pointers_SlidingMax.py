from collections import deque 
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, A, B):
        d = deque()             #stores index 
        mt = []                 #stores data of index 
        for i in range(len(A)):
            #index of first first Max
            if i <B:
                while len(d)!=0 and A[i]>=A[d[-1]]:
                    d.pop()
                d.append(i)
            if i>=B:
                mt.append(A[d[0]])
                while len(d)!=0 and A[i]>=A[d[-1]]:
                   d.pop()
                while len(d)!=0 and d[0]<=i-B:
                    d.popleft()
                d.append(i)
        mt.append(A[d[0]])
        return mt         

        '''
        #Brute-Force
        if B>len(A):
            return [max(A)]
        else:
            mt = []
            i= 0
            j =B-1
            while len(A)>j:
                mt.append(max(A[i:j+1]))
                i+=1
                j+=1
            return mt 
                
         '''       
            
            
if __name__=='__main__':
    n = int(input())
    for i in range(n):
        S = Solution()
        c = list(map(int,input().split(' ')))
        c1 = int(input())
        print (S.slidingMaximum(c,c1))


'''
SLIDINGMAX

A long array A[] is given to you. There is a sliding window of size w
which is moving from the very left of the array to the very right.
You can only see the w numbers in the window. Each time the sliding
window moves rightwards by one position.

Example :

The array is [1 3 -1 -3 5 3 6 7], and w is 3.
Window position 	Max
  	 
[1 3 -1] -3 5 3 6 7 	3
1 [3 -1 -3] 5 3 6 7 	3
1 3 [-1 -3 5] 3 6 7 	5
1 3 -1 [-3 5 3] 6 7 	5
1 3 -1 -3 [5 3 6] 7 	6
1 3 -1 -3 5 [3 6 7] 	7

Input: A long array A[], and a window width w
Output: An array B[], B[i] is the maximum value of from A[i] to A[i+w-1]
Requirement: Find a good optimal way to get B[i]

    Note: If w > length of the array, return 1 element with the max of the array. 

'''

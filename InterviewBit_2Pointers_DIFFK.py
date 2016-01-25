class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        i = 0
        j =  len(A)-1
        if len(A)<2:    return 0
        while  i!=j:
            #print (A[j],A[i])
            diff = A[j]-A[i]
            if diff==B:
                return 1
            i+=1
            if i==j:
                i = 0
                j-=1
        return 0

if __name__=='__main__':
    B = Solution()
    n = int(input())
    for i in range(n):
        c = list(map(int,input().split(' ')))
        #c1 = list(map(int,input().split(' ')))
        c1 = int(input())
        print (B.diffPossible(c,c1))


'''


Given an array ‘A’ of sorted integers and another non negative integer k, find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.

    Example:

    Input : 

    A : [1 3 5] 
    k : 4

    Output : YES

    as 5 - 1 = 4 

Return 0 / 1 ( 0 for false, 1 for true ) for this problem

Try doing this in less than linear space complexity.
'''

class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        B = len(A)
        S = sum(A)
        Sa = sum(i for i in range(1,B+1))
        Sa2 = sum(i*i for i in range(1,B+1))
        S2 = sum(i*i for i in A)
        missing = int((((Sa2-S2)/(Sa-S))+(Sa-S))/2)
        dup = int((((Sa2-S2)/(Sa-S))-(Sa-S))/2)
        #print (Sa2,Sa,S2,S)
        return [dup,missing]
        
            
        
    
if __name__=='__main__':
    n = int(input())
    for i in range(n):
        S = Solution()
        c = list(map(int,input().split(' ')))
        print (S.repeatedNumber(c))


'''
You are given a read only array of n integers from 1 to n.

Each integer appears exactly once except A which appears twice and B which is missing.

Return A and B.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Note that in your output A should precede B.

Example:

Input:[3 1 2 5 3] 

Output:[3, 4] 

A = 3, B = 4

'''

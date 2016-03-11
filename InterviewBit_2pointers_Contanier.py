class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArea(self, A):
        if len(A)==1:   return 0
        i = 0
        area_max = 0
        j=len(A)-1
        while i<j: 
            area_max = max(area_max,(j-i)*min(A[i],A[j]))
            
            if A[i]<A[j]:
                i+=1
            else:
                j-=1
        return area_max


        
if __name__=='__main__':
    n = int(input())
    for i in range(n):
        S = Solution()
        c = list(map(int,input().split(' ')))
        print (S.maxArea(c))
        

'''
CONTAINER

Given n non-negative integers a1, a2, ..., an,
where each represents a point at coordinate (i, ai).
'n' vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).

Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Your program should return an integer which corresponds to the maximum area of water that can be contained ( Yes, we know maximum area instead of maximum volume sounds weird. But this is 2D plane we are working with for simplicity ).

    Note: You may not slant the container. 

Example :

Input : [1, 5, 4, 3]
Output : 6

Explanation : 5 and 3 are distance 2 apart. So size of the base = 2. Height of container = min(5, 3) = 3. 
So total area = 3 * 2 = 6
'''

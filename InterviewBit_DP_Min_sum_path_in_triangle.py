class Solution(object):

    def minimumTotal(self,triangle):
        n = len(triangle)
        for i in range(n-2,-1,-1):
            for j in range(0,i+1):
                triangle[i][j] += min(triangle[i + 1][j],triangle[i + 1][j + 1])
        return triangle[0][0]


if __name__=='__main__':

    S = Solution()
    Tri = []
    for x in range(int(input('Traiangle Height'))):
        Tri+= [list(map(int,input().split(' ')))]
    print  (S.minimumTotal(Tri))
    
        
'''
Min Sum Path in Triangle

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

    Note:
    Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle. 

'''

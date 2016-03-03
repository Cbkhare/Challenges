from sys import argv
class Solution(object):

    def minimumTotal(self,triangle):
        n = len(triangle)
        for i in range(n-2,-1,-1):      #n-2 = n-1 is acutal len
            for j in range(0,i+1):
                #print(i,j)
                triangle[i][j] += max(triangle[i + 1][j],triangle[i + 1][j + 1])
        return triangle[0][0]



if __name__=='__main__':
    
    file_name = argv[1]
    fp = open(file_name,'r')
    M = []
    for line in fp:
        x=(line.strip('\n').split(' '))
        if '' in x:
            while '' in x:  x.pop(x.index(''))
        M.append(list(map(int,x)))
    S = Solution()
    print (S.minimumTotal(M))

'''
Pass Triangle

Challenge Description:

By starting at the top of the triangle and moving to adjacent numbers on the row below, the maximum total from top to bottom is 27.

   5
  9 6
 4 6 8
0 7 1 5

5 + 9 + 6 + 7 = 27
Input sample:

Your program should accept as its first argument a path to a filename. Input example is the following:

You make also check full input file which will be used for your code evaluation.
Output sample:

The correct output is the maximum sum for the triangle. So for the given example the correct answer would be
'''

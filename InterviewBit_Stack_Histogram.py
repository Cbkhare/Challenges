from collections import deque
class Solution:
    # @param A : list of integers
    # @return an integer
    def largestRectangleArea(self, A):
        stack = []
        mx = 0
        last = -1
        area = 0
        i = 0
        while i < len(A):
            if len(stack) == 0 or A[i] >= A[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                last = stack.pop()
                area = A[last]*(i if len(stack) == 0 else i - stack[-1] - 1)
                if mx < area:
                    mx = area
        while len(stack) != 0:
            print (stack)
            last = stack.pop()
            area = A[last]*(i if len(stack) == 0 else i - stack[-1] - 1)
            if mx < area:
                mx = area
        return mx

        
if __name__=='__main__':
    n = int(input())
    for i in range(n):
        S = Solution()
        c = list(map(int,input().split(' ')))
        print (S.largestRectangleArea(c))
        

'''
HISTOGRAM

Given n non-negative integers representing the histogram’s bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

Example Histogram

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

Example2

The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given height = [2,1,5,6,2,3],
return 10.
'''

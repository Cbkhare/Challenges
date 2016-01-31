class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        n = len(A)
        if n == 0:
            return B
        A.sort()
        minDiff = 2147483648
        ret = 0
        for i in range(n):
            j = i + 1
            k = n - 1
            while j < k :
                temp = A[i]+A[j]+A[k]
                diff = abs(temp-B)
                if diff == 0:
                    return temp
                if diff < minDiff:
                    minDiff = diff
                    ret = temp
                if temp <= B:
                    j += 1
                else:
                    k -= 1
        return ret
                

        
if __name__=='__main__':
    B = Solution()
    n = int(input())
    #c  = tuple(map(int,input().split(' ')))
    for i in range(n):
        c  = list(map(int,input().split(', ')))
        m = int(input())
        #c = input()
        print (B.threeSumClosest(c,m))
    

'''
3sum

Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.

Example:
given array S = {-1 2 1 -4},
and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)
'''

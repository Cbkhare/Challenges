class Solution:
    # @return an integer
    def numTrees(self, n):
        if n <= 1:
            return 1
        res = [0 for x in range(n + 1)]
        res[0] = 1
        res[1] = 1
        i = 2
        while i <= n :
            for j in xrange(i):
                res[i] = res[i] + res[j]* res[i-j-1]
            i = i + 1
        return res[n]

if __name__=='__main__':

    n = int(Si.readline())
    S = Solution()
    print(S.numTrees)

'''
Unique Binary Search Trees  
Total Accepted: 81275 Total Submissions: 217341 Difficulty: Medium

Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''

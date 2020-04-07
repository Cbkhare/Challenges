class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        pre = [0, 1]
        # 0 index --> no swap 
        # 1 index --> swap
        for i in range(1, n):
            cur = [sys.maxsize, sys.maxsize]
            if A[i]>A[i-1] and B[i]>B[i-1]:
                # no swap
                cur[0] = min(cur[0], pre[0])
                # no swap with no swap
                cur[1] = min(cur[1], pre[1]+1)
                # no swap with swap
            if A[i]>B[i-1] and B[i]>A[i-1]:
                # swap
                cur[0] = min(cur[0], pre[1])
                # swap with no swap
                cur[1] = min(cur[1], pre[0]+1)
                # swap with swap
            pre = cur
        return min(pre)
    
'''
This problem can be solved using dynamic programming, at each position, we can choose to swap or not. Since we want two sorted arrays, at each position, whether to swap or not depends on the choice at previous position, so we can form a recursive formula.

N = len(A)
dp = [[maxint]*2 for _ in range(N)]

Let initialize a N*2 array dp,

    dp[i][0] means the least swaps used to make A[:i+1] and B[:i+1] sorted having no swap at i-th position.
    dp[i][1] means the least swaps used to make A[:i+1] and B[:i+1] sorted having swap at i-th position.

Picture explanation:
image

Here is the recursive formula:

There are two cases that can make the two arrays sorted:

A . B
C . D

Here our cases are A<B and C<D and A<D and C<B.

Because the possible combination to be sorted are only A B in array1 C D in array2 or A D in array1 C B in array2, so only the 2 cases, and they can holds at the same time: for example A=1, B=2, C=1, D=2. If both don't hold, swapping can't make them in order.

For $i in [1, N]$:

If A[i]>A[i-1] and B[i]>B[i-1] (they are in order without swap):
dp[i][0]=min(dp[i][0], dp[i-1][0]) (no swap at i-1 and no swap at i)
dp[i][1]=min(dp[i][1], dp[i-1][1]+1) (swap at i-1 so swap at i to make in order)

If A[i]>B[i-1] and B[i]>A[i-1] (they are in order with a swap):
dp[i][0]=min(dp[i][0], dp[i-1][1]) (swap at i-1, no need to swap at i)
dp[i][1]=min(dp[i][1], dp[i-1][0]+1) (no swap at i-1, so swap at i)

The two cases don't conflict with each other, so we choose minimum of them when both holds.

What we want to return is min(dp[N-1][0], dp[N-1][1]).

At every recursion, we only need the last result, so we can use less space, from O(N) to O(1), time complexity O(N).
'''

from sys import stdin as S, maxsize as m 
t = int(S.readline())
for i in range(t):
    b = S.readline()
    L = list(map(int,S.readline().split()))

    def nConti(A):
        A.sort()
        Max= A[0]
        for i in range(1,len(A)):
            Max = max(Max,A[i],Max+A[i])
        return Max

    def conti(A):
        A = A[:]
        Max = A[0]
        for i in range(1,len(A)):
            A[i] = max(A[i],A[i]+A[i-1])
            Max = max(A[i],Max)
        return Max

    print (conti(L),nConti(L))
    
'''
Given an array A={a1,a2,…,aN}A={a1,a2,…,aN} of NN elements, find the maximum possible sum of a

    Contiguous subarray
    Non-contiguous (not necessarily contiguous) subarray.

Empty subarrays/subsequences should not be considered.

Input Format

First line of the input has an integer TT. TT cases follow.
Each test case begins with an integer NN. In the next line, NN integers follow representing the elements of array AA.

Constraints:

    1≤T≤101≤T≤10
    1≤N≤1051≤N≤105
    −104≤ai≤104−104≤ai≤104

The subarray and subsequences you consider should have at least one element.

Output Format

Two, space separated, integers denoting the maximum contiguous and non-contiguous subarray. At least one integer should be selected and put into the subarrays (this may be required in cases where all elements are negative).

Sample Input

2 
4 
1 2 3 4
6
2 -1 2 3 4 -5

Sample Output

10 10
10 11

Explanation

In the first case:
The max sum for both contiguous and non-contiguous elements is the sum of ALL the elements (as they are all positive).

In the second case:
[2 -1 2 3 4] --> This forms the contiguous sub-array with the maximum sum.
For the max sum of a not-necessarily-contiguous group of elements, simply add all the positive elements.
'''

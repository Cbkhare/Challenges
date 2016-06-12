from sys import stdin as Si,maxsize as m
from math import ceil as C

def solution(A):
    S =set(A)
    for i in range(len(A)):
        if S.difference(set(A[:i+1]))==set():
            return i


if __name__=='__main__':
    t = int(Si.readline())
    for i in range(t):
        n = list(map(int,Si.readline().split()))
        print (solution(n))

'''


A non-empty zero-indexed array A consisting of N integers is given. The first covering prefix of array A is the smallest integer P such that 0≤P<N and such that every value that occurs in array A also occurs in sequence A[0], A[1], ..., A[P].

For example, the first covering prefix of the following 5−element array A:
A[0] = 2
A[1] = 2
A[2] = 1
A[3] = 0
A[4] = 1

is 3, because sequence [ A[0], A[1], A[2], A[3] ] equal to [2, 2, 1, 0], contains all values that occur in array A.

Write a function

    def solution(A)

that, given a zero-indexed non-empty array A consisting of N integers, returns the first covering prefix of A.

For example, given array A such that
A[0] = 2
A[1] = 2
A[2] = 1
A[3] = 0
A[4] = 1

the function should return 3, as explained above.

Assume that:

        N is an integer within the range [1..1,000,000];
        each element of array A is an integer within the range [0..N−1].

Complexity:

        expected worst-case time complexity is O(N);
        expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).

Elements of input arrays can be modified.
'''

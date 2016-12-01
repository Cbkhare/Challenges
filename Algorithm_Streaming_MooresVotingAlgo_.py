from sys import stdin as si
from collections import Counter as C
from operator import itemgetter as ig
from functools import reduce 
from sys import maxsize as m

class Solution(object):
    def majorityElement(self, A):
        m,c=0,1 
        for i in range(1,len(A)):
            if A[m]==A[i]:
                c+=1
            else:   c-=1
            if c==0:
                m=i
                c=1
        return A[m]

if __name__ == "__main__":
    for i in range(int(si.readline())):
        A = sys.readline().split()
        S = Solution()
        print (S.majorityElement(A))
        

'''
https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm

This is a two step process.
1. Get an element occurring most of the time in the array. This phase will make sure that if there is a majority element then it will return that only.
2. Check if the element obtained from above step is majority element.

1. Finding a Candidate:
The algorithm for first phase that works in O(n) is known as Moore’s Voting Algorithm. Basic idea of the algorithm is if we cancel out each occurrence of an element e with all the other elements that are different from e then e will exist till end if it is a majority element.

findCandidate(a[], size)
1.  Initialize index and count of majority element
     maj_index = 0, count = 1
2.  Loop for i = 1 to size – 1
    (a) If a[maj_index] == a[i]
          count++
    (b) Else
        count--;
    (c) If count == 0
          maj_index = i;
          count = 1
3.  Return a[maj_index]
'''

from operator import itemgetter as ig
from sys import stdin as Si,maxsize as Ms
from itertools import chain
import heapq as Heap


if __name__=='__main__':
    n = int(Si.readline())
    L,H = list(map(int,Si.readline().split())),[]
    Heap.heapify(H)
    for i in range(n):
        if i in [0,1]:
            Heap.heappush(H,L[i])
            print(-1);continue
        elif i==2:
            Heap.heappush(H,L[i])
        else:
            Heap.heappushpop(H,L[i])
        print(H[0]*H[1]*H[2])
    

'''
The Monk learned about priority queues recently and asked his teacher for an interesting problem. So his teacher came up with a simple problem. He now has an integer array A. For each index i, he wants to find the product of the largest, second largest and the third largest integer in the range [1,i].
Note: Two numbers can be the same value-wise but they should be distinct index-wise.

Input:
The first line contains an integer N, denoting the number of elements in the array A.
The next line contains N space separated integers, each denoting the ith integer of the array A.

Output:
Print the answer for each index in each line. If there is no second largest or third largest number in the array A upto that index, then print "-1", without the quotes.

Constraints:
1 <= N <= 100000
0 <= A[i] <= 1000000
SAMPLE INPUT

5
1 2 3 4 5

SAMPLE OUTPUT

-1
-1
6
24
60

Explanation

There are 5 integers 1,2,3,4 and 5.
For the first two indexes, since the number of elements is less than 3, so -1 is printed.
For the third index, the top 3 numbers are 3,2 and 1 whose product is 6.
For the fourth index, the top 3 numbers are 4,3, and 2 whose product is 24.
For the fifth index, the top 3 numbers are 5,4 and 3 whose product is 60.
Time Limit: 1.0 sec(s) for each input file.
Memory Limit: 256 MB
Source Limit: 1024 KB
Marking Scheme: Marks are awarded if any testcase passes.
Allowed Languages: C, CPP, CLOJURE, CSHARP, D, ERLANG, FSHARP, GO, GROOVY, HASKELL, JAVA, JAVA8, JAVASCRIPT, JAVASCRIPT_NODE, LISP, LISP_SBCL, LUA, OBJECTIVEC, OCAML, OCTAVE, PASCAL, PERL, PHP, PYTHON, PYTHON3, R, RACKET, RUBY, RUST, SCALA, SWIFT, VB

'''
            
            

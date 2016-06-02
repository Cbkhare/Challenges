from operator import itemgetter as ig
from sys import stdin as Si,maxsize as Ms
from itertools import chain
import heapq as Heap


if __name__=='__main__':
    n = int(Si.readline())
    H = []
    #Heap.heapify(H) 
    for i in range(n):
        Q = tuple(map(int,Si.readline().split()))
        if Q[0]==1:
            #Heap.heappush(H,Q[1])
            H.append(Q[1])
        elif Q[0]==2:
            if Q[1] in H:
                H.remove(Q[1])
                #Heap.heapify(H)
            else:
                print(-1)

        elif Q[0]==3:
            if H==[]:   print(-1)
            else:       print(max(H))
        elif Q[0]==4:
            if H==[]:   print(-1)
            else:       print(min(H))
            
'''
Monk was asked to answer some queries in an interview. He is given an empty array A. Queries are of 4 types:-
1. 1 X - Add number X to the array A.
2. 2 X - Remove a single instance of number X from the array A. If not possible, print "-1" without the quotes.
3. 3 - Find the maximum element in the array A.
4. 4 - Find the minimum element in the array A.

Input:
The first line contains the integer Q.
The next Q lines will each contain a query like the ones mentioned above.

Output:
For queries 3 and 4, print the answer in a new line. If the array is empty for query 3 and 4, then print "-1" without the quotes.

Constraints:
1 <= Q <= 100000
1 <= X <= 100000
SAMPLE INPUT

5
1 5
1 9
1 6
3
2 1

SAMPLE OUTPUT

9
-1

Explanation

There are 5 queries.
Query 1 - 5 is added to the array.
Query 2 - 9 is added to the array.
Query 3 - 6 is added to the array.
Query 4 - The maximum element in the array is 9.
Query 5 - Since there is no element in the array with value 1, so the output is -1.

'''

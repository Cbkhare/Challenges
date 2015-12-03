class Solution:
    # @param A : list of integers
    # @return a list of integers
    def bin1(self, A,Q):
        s = 0
        e = len(A)-1
        x = -1
        while s<=e:
            m = int((e+s)/2)
            if A[m]==Q:
                x = m
                e = m-1     #for the first occurence, s=m+1 for the last occurence 
            elif A[m]<Q:
                s = m+1
            elif A[m]>Q:
                e = m-1
            
        return x
                

if __name__=='__main__':

    B =Solution()
    #n = int(input())
    n = input().split(' ')
    #lst = tuple(map(int,input().split(' ')))
    lst = input().split(' ')
    lst = tuple(map(int,lst))
    for i in range(int(n[1])):
        #c = list(map(int,input().split(' ')))
        q = int(input())
        print (B.bin1(lst,q))
    exit
'''
Find the first occurence of any given number.
Input
K N
0 1 .... K (elements)
0
1
.
.
N (Queries)

Output
Index of first occurence of the number, -1 if num doesnot exist

example:-
5 4
0 1 1 2 2
1
2
3
0

output:-
1
3
-1
0
'''

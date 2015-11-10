class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        if 0<=A<1:
            return 0
        elif A==1:
            return A
        elif A>1:
            s= 1
            e = A

            while s<=e:
                
                m = int((e+s)/2)
                #print (s,e,m)
                if m*m==A:
                    return m
                if m*m>A:
                    e = m-1
                if m*m<A:
                    s =m+1
            if m*m > A:
                return m-1
            else:
                return m
                

if __name__=='__main__':

    B =Solution()
    n = int(input())
    #s = list(map(int,input().split(' ')))
    for i in range(n):
        #c = list(map(int,input().split(' ')))
        #sup.append(list(map(int,input().split(' '))))
        c = int(float(input()))
        print (B.sqrt(c))

'''
SQRT

Implement int sqrt(int x).

Compute and return the square root of x.

If x is not a perfect square, return floor(sqrt(x))

Example :

Input : 11
Output : 3

DO NOT USE SQRT FUNCTION FROM STANDARD LIBRARY
'''

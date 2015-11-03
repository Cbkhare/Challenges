class Solution:
    # @param A : list of list
    # @return the same list modified
    def rotate(self, A):
        for lst in A:
            lst.reverse()
        l = len(A)

        for i in range(0,l-1):      #l-2 becoz 0 is included
            for j in range(0,l-1-i):
                a=A[i][j]
                b=A[l-1-j][l-1-i]
                #swap
                A[i][j]=b
                A[l-1-j][l-1-i] =a
                
                #one liner
                #A[i][j], A[l-1-j][l-1-i] = A[l-1-j][l-1-i],A[i][j] 

        #for lst in A:
         #   print(lst)
        return A
                

if __name__ == '__main__':

    B = Solution()

    n = int(input())      #matrix size
    inp = list(map(int,input().split(',')))
    #print (inp)
    stack = []
    for t in range(n):
        ss = []
        for nt in range(n):
            ss.append(inp.pop(0))
        stack.append(ss)
    #print (stack)
    print (B.rotate(stack))


'''
Rotate the image by 90 degrees (clockwise).

You need to do this in place.

Note that if you end up using an additional array, you will only receive partial score.


Input :-
4       (nxn matrix)
a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p
[['m', 'i', 'e', 'a'], ['n', 'j', 'f', 'b'], ['o', 'k', 'g', 'c'], ['p', 'l', 'h', 'd']]

output :-


Example:

If the array is

[
    [1, 2],
    [3, 4]
]

Then the rotated array becomes:

[
    [3, 1],
    [4, 2]
]
'''

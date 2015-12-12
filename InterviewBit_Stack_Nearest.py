class Solution:
    # @param arr : list of integers
    # @return a list of integers
    def prevSmaller(self, arr):
        A = arr
        ans = []
        st = []
        for i in range(0,len(A)):
            while st!=[] and st[-1]>=A[i]:
                st.pop(-1)
            if st==[]:
                ans +=[-1]
            else:
                ans+=[st[-1]]
            st.append(A[i])
        return ans 
            
                
             
            
    
if __name__=='__main__':
    n = int(input())
    for i in range(n):
        S = Solution()
        c = list(map(int,input().split(' ')))
        print (S.prevSmaller(c))


'''
Given an array, find the nearest smaller element G[i] for every element A[i] in the array such that the element has an index smaller than i.

More formally,

G[i] for an element A[i] = an element A[j] such that 
    j is maximum possible AND 
    j < i AND
    A[j] < A[i]

Elements for which no smaller element exist, consider next smaller element as -1.

Example:
34 35 27 42 5 28 39 20 28
[-1, 34, -1, 27, -1, 5, 28, 5, 20]

Input : A : [4, 5, 2, 10]
Return : [-1, 4, -1, 2]

Example 2:

Input : A : [3, 2, 1]
Return : [-1, -1, -1]
'''

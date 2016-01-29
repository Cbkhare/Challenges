class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return A modified after the merge 
    def merge(self, A, B):
        i,j=0,0
        stack = []     #new array
        
        while i <len(A) and j<len(B):
            if A[i]<B[j]:
                stack.append(A[i])
                i+=1
            elif A[i]>B[j]:
                stack.append(B[j])
                j+=1
            elif A[i]==B[j]:
                stack += [A[i],B[j]]
                i+=1
                j+=1
        if i<=len(A)-1:          
            #stack +=A[i:]
            while i<len(A):
                stack.append(A[i])
                i+=1
                
        elif j<=len(B)-1:
            #stack+=B[j:]
            while j<len(B):
                stack.append(B[j])
                j+=1
        A = stack
        return A 
if __name__=='__main__':
    B = Solution()
    n = int(input())
    for i in range(n):
        c = list(map(int,input().split(' ')))
        c1 = list(map(int,input().split(' ')))
        print (B.merge(c,c1))


'''


Given two sorted integer arrays A and B, merge B into A as one sorted array.

    Note: You have to modify the array A to contain the merge of A and B. Do not output anything in your code.
    TIP: C users, please malloc the result into a new array and return the result. 

If the number of elements initialized in A and B are m and n respectively, the resulting size of array A after your code is executed should be m + n

Example :

Input : 
         A : [1 5 8]
         B : [6 9]

Modified A : [1 5 6 8 9]

'''

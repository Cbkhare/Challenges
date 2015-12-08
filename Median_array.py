class Solution:
    def BR(self,H,a,b=None):    #boomrang, a=compulsory input,b only needed when h is of size 2
        if len(H)==2:
            if b == None:
                H+=[a]
            else:
                H += [a,b]
            while len(H)>2:
                H.pop(0)
        else:
            if b == None:
                H+=[a]
            else:
                H += [a,b]
            while len(H)>1:
                H.pop(0)
        return H
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def findMedianSortedArrays(self, A, B):
        '''
        m = int((len(A)+len(B)))
        if (m)%2==0:
            H = [0]*2
        else:   H=[0]
        i,j,c = 0,0,0    #A[i],B[j]
        while c<=int((m-1)/2) and i<=len(A)-1 and j<=len(B)-1:
            print (i,j)
            if A[i]==B[j]:
                H = self.BR(H,A[i],B[j])
                i+=1
                j+=1
                c+=2
            elif A[i]>B[j]:
                H = self.BR(H,B[j])
                j+=1
                c+=1
            elif A[i]<B[j]:
                H = self.BR(H,A[i])
                i+=1
                c+=1
        #if c%2==0:
        return H,i,j,c,m
        '''
'''
class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def findMedianSortedArrays(self, A, B):
        m = len(A)
        n = len(B)
        if m > n:
            n,m = m,n
            A,B = B,A
        if m == 0:
            if n == 0:
                return 0
            if n%2:
                return B[n/2]
            else:
                return (B[n/2]+B[n/2-1])/2.0
        low = 0
        high = m
        while low <= high:
            i = (low+high)/2
            j = (m+n+1)/2-i
            if (j == 0 or i == m or B[j - 1] <= A[i]) and (i == 0 or j == n or A[i-1] <= B[j]):
                if (m+n)%2:
                    if i == 0:
                        return B[j-1]
                    elif j == 0:
                        return A[i-1]
                    return max(A[i-1],B[j-1])
                else:
                    if i == 0:
                        return (B[j-1] + min(A[i],B[j]))/2.0
                    if j == 0:
                    	return (A[i-1] + min(A[i],B[j]))/2.0
                    if i == m:
                    	return (max(A[i-1],B[j-1]) + B[j])/2.0
                    if j == n:
                    	return (max(A[i-1],B[j-1]) + A[i])/2.0
                    return (max(A[i-1],B[j-1]) + min(A[i],B[j]))/2.0
            elif (j == 0 or i == m or B[j - 1] > A[i]):
                low = i+1
            elif (i == 0 or j == n or A[i-1] > B[j]):
                high = i-1
        return -1


'''
    
if __name__=='__main__':
    B = Solution()
    n = int(input())
    #c  = tuple(map(int,input().split(' ')))
    for i in range(n):
        c1  = tuple(map(int,input().split(' ')))
        c2  = tuple(map(int,input().split(' ')))
        #m = int(input())
        print (B.findMedianSortedArrays(c1,c2))
    

'''


There are two sorted arrays A and B of size m and n respectively.

Find the median of the two sorted arrays ( The median of the array formed by merging both the arrays ).

The overall run time complexity should be O(log (m+n)).

Sample Input

A : [1 4 5]
B : [2 3]

Sample Output

3

    NOTE: IF the number of elements in the merged array is even, then the median is the average of n / 2 th and n/2 + 1th element.
    For example, if the array is [1 2 3 4], the median is (2 + 3) / 2.0 = 2.5 


'''

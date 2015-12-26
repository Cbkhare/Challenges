class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        if len(A)==1:
            if A[0]>=0:    return A
            else:   return []
        A+=[-1]
        s,sm,e,em=0,0,0,0
        sum_cur = 0
        sum_max = 0
        st = []
        for i in range(len(A)):
            if A[i]>=0:
                sum_cur+=A[i]
                e+=1
            elif A[i]<0 or i==len(A)-1:
                if sum_cur>=sum_max:
                    sum_max=sum_cur       
                    st.append([s,e])
                    sm=s
                    em=e
                sum_cur = 0
                s=i+1
                e=s
        st=st[-2::-1]   #reversing & leaving last sm,se 
        cd = em-sm    #to break tie
        for x,y in st:
            if sum_max==sum(A[x:y]):
                if y-x>cd:
                    sm,em=x,y
                elif y-x==cd:
                    if x<sm:
                        sm,em=x,y                   
                
        return A[sm:em]
            
            
            
        
            
if __name__=='__main__':
    n = int(input())
    for i in range(n):
        S = Solution()
        c = list(map(int,input().split(' ')))
        #c1 = int(input())
        print  (S.maxset(c))

        


'''
MAXSET

Find out the maximum sub-array of non negative numbers from an array.
The sub-array should be continuous. That is, a sub-array created by choosing the second and fourth element and skipping the third element is invalid.

Maximum sub-array is defined in terms of the sum of the elements in the sub-array. Sub-array A is greater than sub-array B if sum(A) > sum(B).

Example:

A : [1, 2, 5, -7, 2, 3]
The two sub-arrays are [1, 2, 5] [2, 3].
The answer is [1, 2, 5] as its sum is larger than [2, 3]

NOTE: If there is a tie, then compare with segment's length and return segment which has maximum length
NOTE 2: If there is still a tie, then return the segment with minimum starting index
'''

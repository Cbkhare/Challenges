class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def threeSum(self, A):
        if len(A)==0:   return []
        stack = []
        A.sort()
        #for i in range(len(A)):
        i =0
        if max(A)<0 or A[len(A)-1]==0:    return []
        while A[i]<=0:
            j = i +1
            k = len(A)-1
            while j<k:
                print (A[i],A[j],A[k])
                Sum = A[i]+A[j]+A[k]
                if Sum==0:
                    s = [A[i],A[j],A[k]]
                    s.sort()
                    stack.append(s)
                    #continue
                if Sum <=0:
                    j+=1
                else:
                    k-=1
            i+=1
        return stack

        
if __name__=='__main__':
    B = Solution()
    n = int(input())
    #c  = tuple(map(int,input().split(' ')))
    for i in range(n):
        c  = list(map(int,input().split(', ')))
        #m = int(input())
        #c = input()
        print (B.threeSum(c))
    

'''
3SumZero



Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:

    Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
    The solution set must not contain duplicate triplets.

    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2) 
'''

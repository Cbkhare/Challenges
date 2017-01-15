class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        if A ==0: return [1]
        if A==1: return [1,1]
        elif A==2: return [1,2,1]
        else:
            old_stack = [1,2,1]
            for i in range(3,A+1):
                stack= [1,]
                for j in range(len(old_stack)-1):
                    stack.append(old_stack[j]+old_stack[j+1])
                old_stack = stack+[1]
                #print (old_stack)
            return old_stack
                

if __name__=='__main__':

    B =Solution()
    n = int(input())
    sup = []
    for i in range(n):
        #c = list(map(int,input().split(' ')))
        #sup.append(list(map(int,input().split(' '))))
        c = int(input())
        print (B.getRow(c))


'''

class Solution(object):
    
    def firstMissingPositive(self, nums):
        n = len(nums)
        for i in range(n):
            if nums[i]<0 or nums[i]>n:  nums[i]=0
        
        for i in range(n):
            if nums[i] not in [0,'x']:
                index = abs(nums[i])
                if nums[index-1] >0:
                    nums[index-1] = -1*nums[index-1]
                #elif nums[index-1]==0:
                    #nums[index-1]='x'  #-10 is an arbitary value
               #nums[nums[i]]<0 signifies that number is present more than once 
        minPositiveNumber = 1

        for i in range(n):
            if nums[i]<0:
                minPositiveNumber +=1
            else:
                break
        
        return minPositiveNumber
'''
'''

Given an unsorted integer array, find the first missing positive integer.

Example:

Given [1,2,0] return 3,

[3,4,-1,1] return 2,

[-8, -7, -6] returns 1

Your algorithm should run in O(n) time and use constant space'''

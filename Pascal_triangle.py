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


Given an index k, return the kth row of the Pascal’s triangle.

Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.

Example:

Input : k = 3

Return : [1,3,3,1]

    NOTE : k is 0 based. k = 0, corresponds to the row [1]. 

Note:Could you optimize your algorithm to use only O(k) extra space?
'''

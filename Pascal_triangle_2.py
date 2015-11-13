class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generate(self, A):
        A= A-1
        if A==0: return [[1]]
        elif A==1: return [[1],[1,1]]
        elif A==2: return [[1],[1,1],[1,2,1]]
        else:
            old_stack = [1,2,1]
            mega_stack= [[1],[1,1],[1,2,1]]
            for i in range(3,A+1):
                stack= [1,]
                for j in range(len(old_stack)-1):
                    stack.append(old_stack[j]+old_stack[j+1])
                old_stack = stack+[1]
                mega_stack.append(old_stack)
            return mega_stack 
                

if __name__=='__main__':

    B =Solution()
    n = int(input())
    #s = list(map(int,input().split(' ')))
    for i in range(n):
        #c = list(map(int,input().split(' ')))
        #sup.append(list(map(int,input().split(' '))))
        c = int(input())
        print (B.generate(c))

'''
PASCAL1

Given numRows, generate the first numRows of Pascal’s triangle.

Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.

Example:

Given numRows = 5,

Return

[
     [1],
     [1,1],
     [1,2,1],
     [1,3,3,1],
     [1,4,6,4,1]
]

'''

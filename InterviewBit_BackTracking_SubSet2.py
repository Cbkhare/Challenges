from itertools import combinations 
class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def bazinga(self,A,stack,size):
        if size==len(A):
            stack.append(A)
            stack.sort()
            return stack
        else:
            for i in (combinations(A,size)):
                #diff with subset1
                if list(i) not in stack:  stack.append(list(i))
            size+=1
            return self.bazinga(A,stack,size)
        
    def subsetsWithDup(self, A):
        if A==[]:   return [[]]
        A.sort()
        stack = [[]]
        return self.bazinga(A,stack,size=1)  
            
if __name__=='__main__':
    n = int(input())
    for i in range(n):
        S = Solution()
        c = list(map(int,input().split(' ')))
        #c1 = input()
        print  (S.subsetsWithDup(c))

      


'''
Given a collection of integers that might contain duplicates, S, return all possible subsets.

    Note:

        Elements in a subset must be in non-descending order.
        The solution set must not contain duplicate subsets.
        The subsets must be sorted lexicographically.

Example :
If S = [1,2,2], the solution is:

[
[],
[1],
[1,2],
[1,2,2],
[2],
[2, 2]
]
'''

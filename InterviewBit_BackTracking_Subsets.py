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
                stack.append(list(i))
            size+=1
            return self.bazinga(A,stack,size)
        
    def subsets(self, A):
        if A==[]:   return [[]]
        A.sort()
        stack = [[]]
        return self.bazinga(A,stack,size=1)

    
if __name__=='__main__':
    n = int(input())
    for i in range(n):
        S = Solution()
        c = list(map(int,input().split(' ')))
        #c = input()
        print (S.subsets(c))
        


'''
SUBSET

Given a set of distinct integers, S, return all possible subsets.

    Note:

        Elements in a subset must be in non-descending order.
        The solution set must not contain duplicate subsets.
        Also, the subsets should be sorted in ascending ( lexicographic ) order.

Example :

If S = [1,2,3], a solution is:

[
  [],
  [1],
  [1, 2],
  [1, 2, 3],
  [1, 3],
  [2],
  [2, 3],
  [3],
]


'''

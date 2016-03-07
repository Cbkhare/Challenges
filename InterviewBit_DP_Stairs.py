class Solution:
    def __init__(self):
        self.g = {0:1,1:1,2:2}
        
    def climbStairs(self,n):

        if n in self.g: return self.g[n]
        else:
            next_step = self.climbStairs(n-1) +\
                        self.climbStairs(n-2)
            self.g[n]=next_step
        return self.g[n]
        
          

if __name__=='__main__':

    S = Solution()
    T = int(input())
    for i in range(T):
        print (S.climbStairs(int(input())))
        

'''
Stairs

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example :

Input : 3
Return : 3

Steps : [1 1 1], [1 2], [2 1]

'''

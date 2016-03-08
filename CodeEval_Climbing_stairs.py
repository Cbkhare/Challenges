from sys import argv 
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
    
    file_name = argv[1]
    fp = open(file_name,'r')
    S = Solution()
    result = ()
    for num in fp:
        result += (str(S.climbStairs(int(num.strip('\n')))),)
    print(' '.join(result))

'''
Challenge Description:

You are climbing a stair case. It takes n steps to reach to the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Input sample:

Your program should accept as its first argument a path to a filename. Each line in this file contains a positive integer which is the total number of stairs.
Ignore all empty lines. E.g.
Output sample:

Print out the number of ways to climb to the top of the staircase. E.g.

Constraints:
The total number of stairs is <= 1000 '''

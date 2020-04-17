class Solution:
    def sum(self, i,s):
        if (i,s) in self.db:
            return self.db[(i,s)]
        
        if i==self.l-1:
            if s==self.S:
                return True, 1 
            else:
                return False, 0
        else: 
            count = 0
            res = self.sum(i+1, s+self.nums[i+1])
            if res[0]:
                count += res[1]
            res = self.sum(i+1, s-self.nums[i+1])
            if res[0]:
                count+=res[1]
            st = False
            if count>0:
                st = True
            self.db[(i,s)] = (st, count)
            return st, count 

    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        self.nums = nums 
        self.l = len(nums)
        self.S = S 
        self.db = {}
        c=0
        res = self.sum(0,0+nums[0])
        c+=res[1]
        res = self.sum(0,0-nums[0])
        c+=res[1]
        return c
        
        

class Solution(object):
    def bazinga(self, i, left_prod):
        temp = self.nums[i]
        if i==self.l-1:
            self.nums[i] = left_prod
            return temp
        else: 
            right_prod = self.bazinga(i+1, left_prod*self.nums[i])
            self.nums[i] = left_prod*right_prod
            return right_prod*temp
            
        
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.l = len(nums)
        self.nums = nums 
        _ = self.bazinga(0,1)
        return self.nums
        

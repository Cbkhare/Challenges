class Solution(object):
    def max_val(self, a, b, nums):
        jump = 1 if a<b else -1
        max_so_far = cur_max = nums[a]
        for i in range(a+jump,b, jump):
            if nums[i]==0:
                cur_max = 0 
            else:
                if cur_max==0:
                    cur_max = nums[i]
                else:
                    cur_max = cur_max * nums[i]
            max_so_far = max(max_so_far, cur_max)
        return max_so_far

    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l<=0:
            return 0
        return max(self.max_val(0,l,nums), self.max_val(l-1,-1, nums))

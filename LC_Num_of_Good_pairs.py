from math import factorial as f


class Solution:

    def numIdenticalPairs(self, nums: list) -> int:
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        count = 0
        for _, v in d.items():
            if v==1: continue
            else:
                count += f(v)//(f(2)*f(v-2))
        return count

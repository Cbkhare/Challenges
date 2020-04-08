class Solution:
    def maxArea(self, h: List[int]) -> int:
        i = 0
        j = len(h)-1
        max_area = -1
        while i<j:
            area = (j-i) * min(h[j],h[i])
            max_area = max(max_area, area)
            if h[j] > h[i]:
                i+=1
            else:
                j-=1
        return max_area

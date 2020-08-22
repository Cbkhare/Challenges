class Solution:
    def numSub(self, s: str) -> int:
        set_one = False
        d = {}
        count = 0
        for i in range(len(s)):

            if s[i] == '1':
                count += 1
                if not set_one:
                    set_one = True
            if s[i] == '0' or i == len(s) - 1:
                if set_one:
                    d[count] = d.get(count, 0) + 1
                    count = 0
                    set_one = False
        total = 0
        print(d)
        for k, v in d.items():
            total += v * (k * (k + 1) // 2)
        return total % (pow(10, 9) + 7)

"""
https://leetcode.com/contest/weekly-contest-197/problems/number-of-substrings-with-only-1s/
"""
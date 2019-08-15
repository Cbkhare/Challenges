from sys import stdin as si


class Solution:
    def __init__(self):
        pass

    def result(self, A):
        l = len(A)
        for i in range(1, l):
            if abs(A[i]-A[i-1]) == 1:
                continue
            else:
                if abs(A[i]-A[i-1]) != l-1:
                    return "NO"
        return "YES"

if __name__=="__main__":
    for i in range(int(si.readline().strip())):
        S = Solution()
        n = si.readline().strip() # pass
        lst = list(map(int, si.readline().strip().split()))
        print (S.result(lst))

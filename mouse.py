from sys import stdin as si


class Solution(object):

    def __init__(self, A):
        self.A = A
        # lookup for memoization
        self.lookup = {}
        self.length = len(A)

    def evaluate(self, i):
        """
        Recursively find the maximum sum
        :param i: integer, index for a self.A
        :return: integer, ans
        """
        if i in self.lookup:
            # if in lookup return ans. Avoid re calculating the ans
            return self.lookup[i]
        if i >= self.length:
            return 0
        self.lookup[i] = self.A[i] + max(self.evaluate(i+2), self.evaluate(i+3))
        return self.lookup[i]

    def print_ans(self):
        """
        prints the ans, i.e  maximum amount of cheese that the mouse can have.
        :return:
        """
        if self.length == 1:
            return self.A[0]
        else:
            print(max(self.evaluate(0), self.evaluate(1)))


if __name__ == "__main__":
    # Reading number for test cases
    for i in range(int(si.readline().strip())):
        _ = si.readline().strip()
        # cheese_blocks is the array
        cheese_blocks = tuple(map(int, si.readline().strip().split()))
        S = Solution(cheese_blocks)
        S.print_ans()

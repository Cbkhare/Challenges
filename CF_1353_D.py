from sys import stdin as si
from heapq import heappop as hpo, heappush as hpu


def evaluate(n):
    x = []
    # pushing on heap on basis of length n, -1* because of min heap,
    # we want n to be first
    hpu(x, (-n, (0, n-1)))
    ans = [0]*n
    for j in range(1, n+1):
        a, cur = hpo(x)
        index = (cur[0] + cur[1])//2
        ans[index] = j
        # print(cur, index)
        # Note at any moment count of arrays of 0 of a given length will always be 2 or < 2
        if cur[0] < index: hpu(x, (-1*(index - 1 - cur[0]), (cur[0], index-1)))
        if cur[1] > index: hpu(x, (-1*(cur[1] - (index + 1)), (index+1, cur[1])))
    print(*ans)


if __name__ == "__main__":
    for i in range(int(si.readline().strip())):
        n = int(si.readline().strip())
        evaluate(n)

from sys import stdin as si

def _dict(n, s):
    d = {}
    for i in range(n):
        d[s[i]] = d.get(s[i], 0) + 1
    return d

def evaluate(d, x):
    count = 0
    for k,v in d.items():
        count += max(v-x, 0)
    return count

if __name__=="__main__":
    for _ in range(int(si.readline().strip())):
        n, q = map(int, si.readline().strip().split())
        d = _dict(n, si.readline().strip())
        for _ in range(q):
            print(evaluate(d, int(si.readline().strip())))

"""
https://www.codechef.com/problems/CORUS
"""

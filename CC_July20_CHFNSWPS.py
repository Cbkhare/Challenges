from sys import stdin as si
from sys import maxsize as m

def solve(n):
    a = list(map(int, si.readline().strip().split()))
    b = list(map(int, si.readline().strip().split()))
    ca = dict()

    # count of each element in both the arrays
    for i in range(n):
        ca[a[i]] = ca.get(a[i], 0) + 1
        ca[b[i]] = ca.get(b[i], 0) - 1
    a = []
    b = []
    mn = m
    for k in sorted(ca.keys()):
        v = ca[k]
        mn = min(mn, k)
        if v%2 != 0:
            return -1
        if v > 0:
            for _ in range(v//2): a.append(k)
        else:
            for _ in range(abs(v)//2): b.append(k)
    b.reverse()
    cost = 0
    for i in range(len(a)):
        cost += min(2*mn, min(a[i], b[i]))
    return cost


if __name__ == "__main__":
    for _ in range(int(si.readline().strip())):
        n = int(si.readline().strip())
        print(solve(n))


'''
8
6
1 3 1 1 3 3
1 3 5 5 5 5 
8
1 1 1 3 3 3 3 2
1 5 5 5 5 2 2 2
3
1 1 1
1 2 2
9
1 1 1 3 3 3 3 3 3
1 5 5 5 5 5 5 5 5
6
1 1 1 1 5 5 1 1
1 1 3 3 4 4 6 6
1
1
2
2
1 2
2 1
2
1 1
2 2


6
1 3 1 1 3 3
1 3 5 5 5 5 
ans:3
8
1 1 1 3 3 3 3 2
1 5 5 5 5 2 2 2
ans:5
3
1 1 1
1 2 2
ans:1
9
1 1 1 3 3 3 3 3 3
1 5 5 5 5 5 5 5 5
ans:7
6
1 1 1 1 5 5 1 1
1 1 3 3 4 4 6 6
ans:3
'''
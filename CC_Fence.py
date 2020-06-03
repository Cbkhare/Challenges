from sys import stdin as si

if __name__ == "__main__":
    for _ in range(int(si.readline().strip())):
        _, _, k = map(int, si.readline().strip().split())
        lookup = {}
        for i in range(k):
            x, y = map(int, si.readline().strip().split())
            def check(d):
                if d in lookup:
                    del lookup[d]
                else:
                    lookup[d] = True
            check((x-1, y-1, x-1, y))
            check((x-1, y-1, x, y-1))
            check((x-1, y, x, y))
            check((x, y-1, x, y))
        print(len(lookup))

"""
https://www.codechef.com/problems/FENCE
"""

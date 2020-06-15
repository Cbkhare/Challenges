from sys import stdin as si


def evaluate(s):
    d = {5: 0, 10: 0, 15: 0}
    for cost in s:
        if cost == 15:
            if d[10] >= 1:
                d[10] -= 1
            elif d[5] >= 2:
                d[5] -= 2
            else:
                print("NO")
                return
            d[15] += 1
        elif cost == 10:
            if d[5] >= 1:
                d[5] -= 1
            else:
                print("NO")
                return
            d[10] += 1
        else:
            d[5] += 1
    print("YES")
    return


if __name__ == "__main__":
    for _ in range(int(si.readline().strip())):
        _ = int(si.readline().strip())
        s = map(int, si.readline().strip().split())
        evaluate(s)

"""
https://www.codechef.com/JUNE20B/problems/CHFICRM
"""


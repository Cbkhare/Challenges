from sys import stdin as si


def evaluate(a, b):
    diff = a-1
    y = b//diff
    z = b % diff
    ans = a * y + z
    if z == 0:
        ans -= 1
    return ans


if __name__=="__main__":
    for i in range(int(si.readline().strip())):
        a, b = map(int, si.readline().strip().split())
        print (evaluate(a,b))

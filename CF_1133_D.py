from sys import stdin as si

# https://github.com/Cbkhare/Algorithms/blob/master/GCD_Euclidean.py
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b%a, a)

def evaluate(n, A, B):
    map = {}
    count = 0
    for i in range(n):
        if B[i] == 0 and A[i] == 0:
            count += 1
            continue
        if A[i] == 0:
            continue
        g = gcd(A[i], B[i])
        d = (-1*B[i]//g, A[i]//g)
        map[d] = map.get(d, 0) + 1
    mx = 0
    #print (map)
    for k, v in map.items():
        mx = max(mx, v)
    return mx + count

if __name__=="__main__":
    n = int(si.readline().strip())
    a = list(map(int, si.readline().strip().split()))
    b = list(map(int, si.readline().strip().split()))
    print(evaluate(n, a, b))

from sys import stdin as si

def evaluate(p,k):
    r = 0
    for i in p:
        r += max(i-k,0)
    print(r)
    return

if __name__ == "__main__":
    for _ in range(int(si.readline().strip())):
        _, k = map(int, si.readline().strip().split())
        p = map(int, si.readline().strip().split())
        evaluate(p,k)


"""
https://www.codechef.com/JUNE20B/submit/PRICECON
"""

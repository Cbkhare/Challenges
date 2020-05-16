from sys import stdin as si


def evaluate(a, b, c, d):
    count = 0
    for i in range(max(c+1, a+b), b+c+1):
        count += (min(d + 1, i) - c) * (min(i - b, b) - max(i - c, a) + 1)
    return count

if __name__ == "__main__":
    #for i in range(int(si.readline().strip())):
    a, b, c, d = map(int, si.readline().strip().split())
    print(evaluate(a, b, c, d))
    #print(binsearch(a,b,c,d))

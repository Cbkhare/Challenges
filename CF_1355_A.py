from sys import stdin as si


def evaluate(n, k):
    num = n
    for i in range(1, k):
        ls = list(map(int, list(str(num))))
        mx = max(ls)
        mn = min(ls)
        if mn == 0:
            return num
        num = num + mn*mx
    return num


if __name__ == "__main__":
    for i in range(int(si.readline().strip())):
        a, k = map(int, si.readline().strip().split())
        print(evaluate(a, k))

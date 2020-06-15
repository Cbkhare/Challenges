from sys import stdin as si


def make_list(n, s, d, num):
    for k in range(n, s, 2):
        d[k] = num
        num += 2
    return num


def evaluate(s):
    odd = 1
    even = 2
    for i in range(s):
        d = [0]*s
        if (i+1)%2 != 0:
            odd = make_list(0,s,d,odd)
            even = make_list(1,s,d,even)
        else:
            odd = make_list(1,s,d,odd)
            even = make_list(0,s,d,even)
        print(*d)
    return


if __name__ == "__main__":
    for _ in range(int(si.readline().strip())):
        s = int(si.readline().strip())
        evaluate(s)


"""
https://www.codechef.com/JUNE20B/problems/EVENM
"""

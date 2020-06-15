from sys import stdin as si


def evaluate(s):
    pair = 0
    p1 = None
    reset = False
    for i in range(len(s)):
        if not reset:
            p1 = s[i]
            reset = True
            continue

        if (p1 == "x" and s[i] == "y") or (p1 == "y" and s[i] == "x"):
            pair += 1
            reset = False
    print(pair)
    return


if __name__ == "__main__":
    for _ in range(int(si.readline().strip())):
        s = si.readline().strip()
        evaluate(s)

"""
https://www.codechef.com/JUNE20B/submit/XYSTR
"""


from sys import stdin as si


def winner(a, b):
    if a//2 < b:
        print(1)
    else:
        print(0)


if __name__ == "__main__":
    for _ in range(int(si.readline().strip())):
        a, b = map(int, si.readline().strip().split())
        winner(a,b)
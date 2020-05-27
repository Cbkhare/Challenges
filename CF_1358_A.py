from sys import stdin as si
from math import ceil

if __name__ == "__main__":
    for i in range(int(si.readline().strip())):
        n, m = map(int, si.readline().strip().split())
        print(ceil(n*m/2))

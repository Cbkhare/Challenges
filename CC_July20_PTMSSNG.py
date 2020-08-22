from sys import stdin as si

def solve(n):
    x = dict()
    y = dict()
    for i in range(n):
        px, py = map(int, si.readline().strip().split())
        x[px] = x.get(px, 0) + 1  # alternate x.get(px, []) + [(px,py)]
        y[py] = y.get(py, 0) + 1  # alternate y.get(py, []) + [(px,py)]
    notX = [k for k, v in x.items() if v % 2 != 0]  # alternate len(v)%2 != 0]
    notY = [k for k, v in y.items() if v % 2 != 0]  # alternate len(v)%2 != 0]
    print(notX[0], notY[0])


if __name__ == "__main__":
    for _ in range(int(si.readline().strip())):
        n = int(si.readline().strip())
        solve(4*n-1)

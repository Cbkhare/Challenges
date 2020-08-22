from sys import stdin as si

def solve(gen):
    last = None
    total = 0
    for j in gen:
        if not last:
            last = j
            continue
        if j != last:
            total += abs(last-j)-1
        last = j
    print(total)


if __name__ == "__main__":
    for _ in range(int(si.readline().strip())):
        _ = si.readline().strip()
        gen = map(int, si.readline().strip().split())
        solve(gen)
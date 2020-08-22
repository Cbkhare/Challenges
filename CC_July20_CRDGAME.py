from sys import stdin as si


if __name__ == "__main__":
    for _ in range(int(si.readline().strip())):
        i = int(si.readline().strip())
        c, m = 0, 0
        for _ in range(i):
            vc, vm = si.readline().strip().split()
            sc = sum(map(int, vc))
            sm = sum(map(int, vm))
            if sc > sm:
                c+=1
            elif sc < sm:
                m+=1
            else:
                c+=1;m+=1
        if c > m:
            print(0, c)
        elif m > c:
            print(1, m)
        else:
            print(2, c)
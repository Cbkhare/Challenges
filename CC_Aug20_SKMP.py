from sys import stdin as si


def pre_dict(a):
    d = {}
    for c in a:
        d[c] = d.get(c, 0) + 1
    return d


def solve(s, p):
    sd = pre_dict(s)
    sp = pre_dict(p)
    for c in sp:
        sd[c] -= sp[c]
        if sd[c] == 0:
            del sd[c]
    if len(sd) == 0:
        return p
    pre = ''
    del_list = []
    mn = True
    for i in range(1, len(p)):
        if ord(p[i]) == ord(p[i-1]):
            continue
        if ord(p[i]) < ord(p[i-1]):
            mn = False
        break
    for k, v in sd.items():
        if mn:
            if ord(k) <= ord(p[0]):
                pre += k*v
                del_list.append(k)
        else:
            if ord(k) < ord(p[0]):
                pre += k*v
                del_list.append(k)
    for d in del_list:
        del sd[d]
    suf = ''
    for k, v in sd.items():
        suf += k*v
    return ''.join(sorted(pre)) + p + ''.join(sorted(suf))


if __name__ == "__main__":
    for _ in range(int(si.readline().strip())):
        s = si.readline().strip()
        p = si.readline().strip()
        print(solve(s, p))
if __name__=='__main__':
    s = input()
    k = int(input())
    Set = set(s)
    C = []
    for ss in Set:
        C.append(s.count(ss))
    while k>0 and C!=[]:
        m = max(C)
        C.remove(m)
        if m-1<0:
            break
        else:
            C+=[m-1]
            k-=1
    print (sum([x**2 for x in C]))
        

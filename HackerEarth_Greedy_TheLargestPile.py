from operator import itemgetter as ig
from sys import stdin as Si,maxsize as Ms
from itertools import chain

def longestToN(n,I,T):
    m = 0
    for i in range(n,-1,-1):
        if I[i]>I[n]:
            if T[i]==-1:
                T[i]=longestToN(i,I,T)
            m = max(m,1+T[i])
    return m


def LDS(I):
    l = len(I)
    T = [-1 for i in range(l)]
    m=0
    for n in range(l):
        if T[n]==-1:
            T[n] = longestToN(n,I,T)
        m = max(m,longestToN(n,I,T))
    return m+1,T
    
if __name__=='__main__':
    '''
    n = int(Si.readline())
    H = tuple(map(int,Si.readline().split()))
    G = tuple(map(int,Si.readline().split()))
    Gold,Height,last,long = G[0],H[0],0,[0]
    Ind = sorted(range(n), key = lambda k: H[k])
    '''
    Ind = list(map(int,Si.readline().split()))
    S = LDS(Ind)
    print(S)


'''
    for i in range(1,n):
        print(Gold,Height,G[i],H[i])
        if H[i]>H[last] and G[i]>G[last]:
                Gold=G[i];Height=H[i];last = i;long = [last]
        elif G[i]==Gold:
            if Height<=H[i]:    last=i;long=[last]
        else:
            if H[i]<H[last]:
                Gold+=G[i];Height+=H[i];last=i;long.append(i)
            else:
                if G[i]<=G[last]:    continue #ignore
                else:
                    OG = Gold #original Gold 
                    while G[i]+Gold-G[last]>OG and H[i]>H[last]:
                        Gold-=G[last];Height-=H[last]
                        long.pop(-1)
                        last=long[-1]
                    Gold+=G[i];Height+=H[i];last=i;long.append(i)
        print(Gold,Height)
                    
'''




            
'''
         print (des,Height,Gold)
            if H[i]<H[last]:
                if G[i]<G[last]:
                    Gold+=G[i];Height+=H[i];last=i;long.append(i)
                else:
                    Gold,Height,long=G[long[0]],H[long[0]],[long[0]]
                    for j in range(long[0]+1,i+1):
                        if H[j]>H[i] and G[i]>G[j]:
                            Height+=H[j];Gold+=G[j];long.append(j)
                    last=i
            else:
                if G[i]>G[last]:
                    while H[i]>H[last] and G[i]>G[last]:
                        Gold-=G[last];Height-=H[last]
                        long.pop(-1);last=long[-1]
                    Gold+=G[i];Height+=H[i];last=i;long.append(i)
                else:   continue 

'''

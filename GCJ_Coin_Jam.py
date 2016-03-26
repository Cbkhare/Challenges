from sys import stdin as Si
from math import sqrt; from itertools import count, islice
from itertools import permutations 

if __name__=='__main__':
    '''
    def isPrime(n):
        return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))
    '''
    def isPrime(n):
        if n < 2: return False
        for number in islice(count(2), int(sqrt(n)-1)):
            if not n%number:
                return (False,number)
        return (True,1)

    def getBases(S):
        B = []
        for i in range(2,11):
            _S,Nu = S[::-1],0
            for j in range(len(S)):
                Nu+= int(S[j])*pow(i,j)
            B.append(Nu)
        return B
    
    def unique_permutations(iterable, r=None):
        previous = tuple()
        for p in permutations(sorted(iterable), r):
            if p > previous:
                previous = p
                yield p

  
    n = int(Si.readline())
    Prime = [] 
    for i in range(n):
        N,J = map(int,Si.readline().split())
        Nums,_n = {},0
        while _n <=N:
            NT = '1'*(N-_n)+'0'*_n
            D = unique_permutations(NT,N)
            for d in D:
                d =''.join(d)
                if d[0]!='1' or d[-1]!='1':    continue
                Bx = getBases(d)
                Px,Tar = [],True
                for b in Bx:
                    if b==1:    continue 
                    V = (isPrime(b))
                    if V[0]:
                        Tar = False;break
                    else:   Px.append(V[1])
                if Tar: Nums[d] = Px
                if len(Nums)==J:    break
            _n+=1
        print('Case #%d:'%(i+1))
        for k,v in Nums.items():
            print (k,v)
        
                    
                

    

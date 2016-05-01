    from sys import stdin as Si
    from fractions import gcd as G
     
    def L(a,b): return (a*b//G(a,b))
     
    if __name__=='__main__':
        n,m = map(int,Si.readline().split(' '))
        S = list(map(int,Si.readline().split(' ')))
        
        Hash = {}
     
        for i in range(n):
            for j in range(i+1,n):
                key = L(S[i],S[j])
                if key<=m:
                    if key not in Hash: Hash[key]=[i]
                    if i not in Hash[key]:   Hash[key].append(i)
                    if j not in Hash[key]:   Hash[key].append(j)
     
     
        #to get longest list which will be longest-sub-seq
        ans_key = max(Hash,key=lambda x:len(Hash[x]))
        Hash[ans_key].sort()
        print ('L.C.M -',ans_key)
        ans_lst = [S[i] for i in Hash[ans_key]]
        print ('Longest sub-seq - ', ans_lst)

'''
Given an array of elements and number M, how can one find the longest sub-sequence of the array with Least Common Multiple lesser or equal to M?

For example:

    Input:
    array size=7, M=8
    array = [6 2 9 2 7 2 3]
    Output:
    LCM = 6 (<=M), sub-sequence size of given array = 5
    Longest Sub-sequence = [6 2 2 2 3]
'''
    
            
            
    
    
        
        


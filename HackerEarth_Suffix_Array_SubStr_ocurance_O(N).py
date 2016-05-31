from operator import itemgetter as ig
from sys import stdin as Si,maxsize as Ms
from itertools import chain
    
if __name__=='__main__':
    S = Si.readline().strip()
    P = Si.readline().strip()

    i,j=0,len(P)-1
    pos = []
    while j<len(S):
        if S[i:j+1]==P:
            pos.append(str(i))
        i+=1;j+=1
    print(' '.join(pos))
    
        
        
'''
#APPLIED 2-Pointers


Suffix Array - Substring Occurrences

Given a string S
and string P, find all the indices of occurrence of T in S

. Follow 0-based indexing of string.

Input:
First line contains string S
.
Second line contains string T

.

Output:
Print all the indices separated by space.

Constraints:
1≤|S|味1000
'''
            

    

        
        
        
        
        
 

from sys import stdin as  Si
from math import ceil

def baz9(Nn,p):
    while Nn[p]=='9':
        Nn[p]=Nn[-p-1]='0'
        p-=1
    Nn[p]=str(int(Nn[p])+1)
    Nn[-p-1]=Nn[p]    #since palin
    return Nn


if __name__=='__main__':
    n = int(Si.readline())
    for _ in range(n):
        N = list(Si.readline().strip('\n'))
        l = len(N)
        if l==1 and '9' not in N: print(int(''.join(N))+1)
        elif l==N.count('9'):  print(int(''.join(N))+2)
        elif N==N[::-1]:
            pos = ceil(l/2)-1  #-1 since zero based list 
            if l%2!=0:
                if N[pos]!='9':
                    N[pos]=str(int(N[pos])+1)
                else:
                    N=baz9(N,pos)
                N = ''.join(N)
            else:
                if N[pos]!='9':
                    N[pos]=str(int(N[pos])+1)*2
                    rN = ''.join(N[:pos][::-1])
                    N = ''.join(N[:pos])+N[pos]+rN
                else:
                    N= ''.join(baz9(N,pos))
            print (N)
        else:   #Not palin
            pos = ceil(l/2)-1
            if l%2!=0:  
                p1,nn,p2 = N[:pos], N[pos],N[pos+1:]
                ip1,ip2= int(''.join(p1[::-1])),int(''.join(p2))
                if ip1>ip2 :
                    N = ''.join(p1)+nn+''.join(p1[::-1])
                elif ip1<ip2:
                    if nn!='9':
                        N = ''.join(p1)+str(int(nn)+1)+''.join(p1[::-1])
                    else:
                        N = baz9(N,pos)
                        rN = ''.join(N[:pos][::-1])
                        N = ''.join(N[:pos])+N[pos]+rN
                print(N)
            else:
                p1,p2 = N[:pos+1],N[pos+1:]
                ip1,ip2= int(''.join(p1[::-1])),int(''.join(p2))
                if ip1>ip2:
                    N = ''.join(p1)+''.join(p1[::-1])
                elif ip1<ip2:
                    nn = ''.join(N[pos:pos+2])
                    if nn[0]!='9': #'9' not in nn:
                        #if int(nn[0])>int(nn[1]):   nn=nn[0]*2
                        #else:   nn=nn[1]*2
                        nn=str(int(nn)+1)
                        while nn[0]!=nn[1]: nn=str(int(nn)+1)
                        N = ''.join(p1[:-1])+nn+''.join(p1[::-1][1:])
                    else:
                        if nn=='99' or nn[0]=='9':
                            N = ''.join(baz9(N,pos))
                            rN = N[:pos+1][::-1]
                            N = N[:pos+1]+''.join(rN)
                        '''
                        elif nn[1]=='9' and nn[0]!='9':
                            if int(nn[0])>int(nn[1]):   nn=nn[0]*2
                            else:   nn=nn[1]*2
                            N = ''.join(p1[:-1])+nn+''.join(p1[::-1][1:])
                        '''
                print(N)
    
                        
                    
'''
PALIN - The Next Palindrome
#ad-hoc-1

A positive integer is called a palindrome if its representation in the decimal system is the same when read from left to right and from right to left. For a given positive integer K of not more than 1000000 digits, write the value of the smallest palindrome larger than K to output. Numbers are always displayed without leading zeros.
Input

The first line contains integer t, the number of test cases. Integers K are given in the next t lines.
Output

For each K, output the smallest palindrome larger than K.
Example

Input:
2
808
2133

Output:
818
2222
'''

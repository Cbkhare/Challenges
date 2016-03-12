from sys import maxsize as m
class Solution:

    def bazinga(self,A):
        MaxA,mst,j,n=0,[],0,len(A)
        j= 0
        while j<n:  #len(stack)
            if A[j]==0:
                j+=1
            else:
                k = j+1
                while k<n:
                    if A[k]==0: break
                    k+=1
                M = A[j:k]
                x=0
                while x <(k-j):
                    print(M)
                    if mst==[] or M[x]>=M[mst[-1]]: mst.append(x)
                    elif M[x]<M[mst[-1]]:
                        print(mst)
                        while (mst and M[x]<=M[mst[-1]]):
                            print(MaxA)
                            MaxA=max(MaxA,M[mst.pop(-1)]*(x if not mst else x-mst[-1]-1))
                        mst.append(x)
                    x+=1
                    if x==k-j and mst!=[]:  #Final
                        l=len(M)
                        while mst and l<=len(mst):
                            MaxA = max(MaxA,M[mst.pop(0)]*(l))
                            l-=1
                j = k
        return (MaxA)
          

if __name__=='__main__':

    S = Solution()
    T = int(input())
    for i in range(T):
        print (S.bazinga(list(map(int,input().split(' ')))))
        
            
'''
Rectangle with max area in a histogram

0 2 3 4 2
ans 8
'''
        
        
    
        

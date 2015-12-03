from operator import itemgetter as ig
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        if len(A)==0:   return -1
        #print (A)
        G= {}
        for e in range(len(A)):
            G[e] = A[e]

        #G= sorted(G.items(),key=ig(0))
        G= sorted(G.items(),key=ig(1))
        print (G)
        s = 0   #max sub 
        for x in range(len(G)-1):
            #m = max(G[x:],key=ig(1))
            m = max(G[x+1:],key=ig(0))  #finding max 
            cc = G.index(m) +1          #needed when there are common elements
            st = 0
            con = 0
            if con==0:
                st = m[0]-G[x][0]   #last value of GL - current value
            else:
                st = m[0]-G[x][0]
            if st >= s:
                print (st,cc)
                s = st
        return s
            
        '''
        Method 2, Non-linear time complexity
        
        if len(A)==0:   return -1    #since condition is j-i, for j==i, A[i]<=A[j]
        i,j = 0,0
        s = [0]
        while j <= len(A)-1:
            
            for x in range(i,len(A)):
                #print (i,j,A.index(A[x]),A[x:].index(A[x]))
                if A[x]>=A[i]:
                    s.append(x-i)
            i +=1
            j +=i
        return max(s)
        '''

        
if __name__=='__main__':

    B =Solution()
    n = int(input())
    #s = list(map(int,input().split(' ')))
    for i in range(n):
        c = list(map(int,input().split(' ')))
        #sup.append(list(map(int,input().split(' '))))
        print (B.maximumGap(c))

        
'''        


Given an array A of integers, find the maximum of j - i subjected to the constraint of A[i] <= A[j].

If there is no solution possible, return -1.

Example :

A : [3 5 4 2]

Output : 2 
for the pair (3, 4)


'''

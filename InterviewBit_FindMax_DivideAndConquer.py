from sys import stdin as si

class Solution:
    # @param A : list of integers
    # @return an integer
    def sol(self,i,j,M):
        self.count +=1
        if i==j:    return self.A[i]
        elif i==j-1:    return max(self.A[i],self.A[j])
        else:
            m = int((i+j)/2)
            M1 = self.sol(i,m,M)
            M2 = self.sol(m+1,j,A[m])
            return max(M1,M2)
        
    def solve(self,A):
        self.count = 0 
        self.A = A
        ans = self.sol(0,len(self.A)-1,self.A[0])
        print (self.count)
        return ans 


if __name__ == "__main__":
    for i in range(int(si.readline())):
        A = [ i for i in range(100)]

        S = Solution()
        print (S.solve(A))

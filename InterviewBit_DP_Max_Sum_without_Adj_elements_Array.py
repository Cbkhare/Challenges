from sys import maxsize as m
class Solution:
    def __init__(self):
        self.g = {}


    def bazinga(self,A,i):
        mSum= -m
        if i in self.g:     return self.g[i]
        elif i+2>=len(A):   self.g[i]=A[i]
        else:
            for j in range(i+2,len(A)):
                mSum = max(self.bazinga(A,j)+A[i],mSum)
            self.g[i]=mSum
        return self.g[i]

    def adjacent(self,A):
        Max = -m
        for i in range(len(A)):
            Max = max(Max,self.bazinga(A,i))
        return Max

if __name__=='__main__':
    T = int(input())
    for i in range(T):
        S = Solution()
        print (S.adjacent(list(map(int,input().split(' ')))))

'''
Max Sum of elements which are not adjacent to each other

3 2 7 10
13
2 7 2 10
17
5 19 5
19
'''
        

